from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from services.auth import logged_in
from services.token_service import TokenService
from .models import Cart


class CartView(GenericAPIView):

    @method_decorator(logged_in)
    def get(self, request, *args, **kwargs):
        smd = {
            'success': True,
            'message': 'Successfully retrieved Cart',
            'data': []
        }
        import pdb
        pdb.set_trace()
        token = request.headers.get('token')
        payload = TokenService().decode_token(token)
        user_id = payload.get('id')
        try:
            cart = Cart.objects.get(customer_id=user_id, order_placed=False)
            if cart is not None:
                smd['data'] = cart.
                return Response(data=smd, status=status.HTTP_200_OK)
        except Exception:
            pass
