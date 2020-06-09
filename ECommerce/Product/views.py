import logging
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from services.aws_services import AwsServices
from services.auth import logged_in, is_admin
from services.token_service import TokenService
from .models import Product
from .serializers import ProductSerializer, OrderProductSerializer
import pdb

# Create your views here.
logging.basicConfig(level=logging.DEBUG)


class ProductsView(GenericAPIView):

    serializer_class = ProductSerializer

    # @method_decorator(logged_in, name='dispatch')
    def get(self, request, *args, **kwargs):
        all_products = Product.objects.all()  # TODO-> Send Presigned Url on GET METHOD.
        smd = {
            'success': True,
            'message': "Successfully retrieved all products",
            'data': all_products.values()
        }
        return Response(data=smd, status=status.HTTP_200_OK)

    @method_decorator(is_admin)
    def post(self, request, *args, **kwargs):

        # if request.data.get('images') is None:
        serializer = ProductSerializer(data=request.data)
        # else:

        # if serializer.is_valid():
        pdb.set_trace()
        if request.data.get('images') is not None:
            img_file = request.data.get('images')
            url = AwsServices().upload_img(img_file, request.data.get('name'))
            serializer.initial_data['images'] = url
        if serializer.is_valid():
            serializer.save()
            logging.info('Product has been created')
            smd = {'success': True, 'message': 'Successfully created product', 'data': []}
            return Response(data=smd, status=status.HTTP_200_OK)
        else:
            logging.info(f'ERROR : {serializer.errors}')
            smd = {'success': False, 'message': 'Unsuccessful in creating product', 'data': []}
            return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)


class SingleProductView(GenericAPIView):

    serializer_class = ProductSerializer

    # @logged_in
    def get(self, request, *args, **kwargs):
        try:
            # pdb.set_trace()
            id = kwargs.get('id')
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
        product_id = args[1].get('id')
        serializer = ProductSerializer(data=request.data, partial=True)

        if serializer.is_valid():
            pass
        pass

    @method_decorator(is_admin)
    def delete(self, request, *args, **kwargs):
        smd = {
            'success': False,
            'message': 'Could Not Delete Product',
            'data': []
        }
        try:
            product_id = args[1].get('id')
            if product_id is None:
                raise ValueError('Could not read product ID from URL')
            product = Product.objects.get(pk=product_id)
            product.delete()
            smd['success'], smd['message'] = True, f'Successfuly Deleted {product.name} '
            return Response(data=smd, status=status.HTTP_200_OK)
        except ValueError:
            smd['data'] = ValueError
            return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)


class OrderView(GenericAPIView):

    serializer_class = OrderProductSerializer

    def post(self, request):
        pass

    def put(self, request, id):
        pass

