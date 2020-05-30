from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from services.auth import logged_in
from services.token_service import TokenService
from .models import Product, Cart
from .serializers import ProductSerializer
import pdb

# Create your views here.


@method_decorator(logged_in, name='dispatch')
class ProductsView(GenericAPIView):

    def get(self, request):
        all_products = Product.objects.all()
        smd = {
            'success': True,
            'message': "Successfully retrieved all products",
            'data': all_products.values()
        }
        return Response(data=smd, status=status.HTTP_200_OK)

    def post(self, request):
        pass


@method_decorator(logged_in, name='dispatch')
class SingleProductView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        try:
            id = args[1].get('id')
            product = Product.objects.get(pk=id)
            serializer = ProductSerializer(product)
            smd = {
                'success': True,
                'message': f'Successfully retrieved product with ID={id}',
                'data': serializer.data
            }
            return Response(data=smd, status=status.HTTP_200_OK)
        except Product.DoesNotExist as err:
            return Response(data={
                'success': False,
                'message:': 'Could Not Retrieve Data',
                'data': f"Product with ID={args[1].get('id')} Does not Exist"
                 },
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass


@method_decorator(logged_in, name='dispatch')
class CartView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        try:
            pdb.set_trace()
            smd = {
                'success': False,
                'message': 'Could not retrieve cart',
                'data': []
            }
            token = request.headers.get('token')
            payload = TokenService().decode_token(token)
            id = payload.get('id')
            cart = Cart.objects.filter(customer_id=id).latest('pk')
            smd['success'], smd['message'], smd['data'] = True, 'Retrieved Cart', []
            return Response(data=None)
        except Cart.DoesNotExist:
            return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)
