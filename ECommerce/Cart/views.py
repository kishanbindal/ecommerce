from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from Product.models import OrderProduct
from services.auth import logged_in
from services.token_service import TokenService
from services.sms_service import SmsService
from Users.models import User
from .models import Cart
from .serializers import CartViewSerializer
import pdb


class CartView(GenericAPIView):

    @method_decorator(logged_in)
    def get(self, request, *args, **kwargs):
        smd = {
            'success': True,
            'message': 'Successfully retrieved Cart',
            'data': []
        }
        # pdb.set_trace()
        try:
            token = request.headers.get('token')
            payload = TokenService().decode_token(token)
            user_id = payload.get('id')
            cart = Cart.objects.get(customer_id=user_id, order_placed=False)
            if cart is not None:
                serializer = CartViewSerializer(cart)
                smd['data'] = serializer.data
                return Response(data=smd, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            smd['success'], smd['message'] = True, 'Cart Is Empty'
            return Response(data=smd, status=status.HTTP_200_OK)
        except Exception:
            pass


class CartOperationsView(GenericAPIView):

    @method_decorator(logged_in)
    def patch(self, request, *args, **kwargs):

        smd = {
            'success': False,
            'message': 'Unable to update cart',
            'data': []
        }
        try:
            id = args[1].get('id')
            cart = Cart.objects.get(pk=id)
            serializer = CartViewSerializer(data=request.data, partial=True)

            if serializer.is_valid():
                serializer.update(cart, serializer.validated_data)
                if cart.order_placed is True:
                    user = User.objects.get(pk=cart.customer.id)
                    OrderProduct.objects.filter(customer_id=user.pk, is_billed=False).update(is_billed=True)
                    SmsService().send_order_placed_sms(user, cart)
                    smd['success'], smd['message'] = True, 'Order Has Been Placed Successfully'
                    return Response(data=smd, status=status.HTTP_200_OK)
                smd['success'], smd['message'] = True, 'Successfully Updated Cart'
                return Response(data=smd, status=status.HTTP_200_OK)
        except Exception as e:
            pass
