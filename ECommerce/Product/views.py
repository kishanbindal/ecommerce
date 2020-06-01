from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from services.auth import logged_in, is_admin
from services.token_service import TokenService
from .models import Product
from .serializers import ProductSerializer
import pdb

# Create your views here.


class ProductsView(GenericAPIView):

    # @method_decorator(logged_in, name='dispatch')
    def get(self, request):
        all_products = Product.objects.all()
        smd = {
            'success': True,
            'message': "Successfully retrieved all products",
            'data': all_products.values()
        }
        return Response(data=smd, status=status.HTTP_200_OK)

    # @method_decorator(is_admin, name='admin post')
    def post(self, request):
        pass


class SingleProductView(GenericAPIView):

    # @logged_in
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


class OrderView(GenericAPIView):

    def get(self, request, id):
        pass

    def post(self):
        pass

    def put(self, request, id):
        pass

