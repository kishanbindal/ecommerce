from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from services.auth import logged_in
from services.token_service import TokenService
from .models import Cart
from .serializer import CartViewSerializer
import pdb


class CartView(GenericAPIView):

    @method_decorator(logged_in)
    def get(self, request, *args, **kwargs):
        smd = {
            'success': True,
            'message': 'Successfully retrieved Cart',
            'data': []
        }
        pdb.set_trace()
        try:
            token = request.headers.get('token')
            payload = TokenService().decode_token(token)
            user_id = payload.get('id')
            cart = Cart.objects.get(customer_id=user_id, order_placed=False)
            if cart is not None:
                serializer = CartViewSerializer(cart)
                smd['data'] = serializer.data
                return Response(data=smd, status=status.HTTP_200_OK)
        except Exception:
            pass
