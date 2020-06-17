import logging
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from services.aws_services import AwsServices
from services.auth import logged_in, is_admin
from services.token_service import TokenService
from .models import Product, OrderProduct
from .serializers import ProductSerializer, OrderProductSerializer, OrderSerializer
from Cart.models import Cart
from Users.models import User
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
        if request.data.get('images') is not None:
            img_file = request.data.get('images')
            url = AwsServices().upload_img(img_file, request.data.get('name'))
            url = AwsServices().get_presigned_url(request.data.get('name'))
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
            pdb.set_trace()
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
                'data': f"Product with ID={kwargs.get('id')} Does not Exist"
                 },
                status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(is_admin)
    def put(self, request, *args, **kwargs):

        smd = {
            'success': False,
            'message': 'Unable to update Product Data',
            'data': []
        }
        try:
            product_id = kwargs['id']
            if type(request.data.get('images')) is not str:
                url = AwsServices().upload_img(request.data.get('images'), request.data.get('name'))
                request.data['images'] = url
            serializer = ProductSerializer(data=request.data, partial=True)
            product = Product.objects.get(pk=product_id)

            if serializer.is_valid():
                serializer.update(product, serializer.validated_data)
                smd['success'], smd['message'] = True, f'Successfully Updated {product.name}'
                return Response(data=smd, status=status.HTTP_200_OK)
            else:
                smd['data'] = serializer.errors
                return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)

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

    @method_decorator(logged_in, name='dispatch')
    def get(self, request, *args, **kwargs):

        smd = {
            'success': False,
            'message': 'Unsuccessful in retrieving orders of user',
            'data': []
        }
        try:
            # pdb.set_trace()
            token = request.headers.get('token')
            payload = TokenService().decode_token(token)
            user_id = payload.get('id')
            orders = OrderProduct.objects.filter(customer_id=user_id, is_billed=False)
            serializer = OrderSerializer(orders, many=True)
            smd['success'], smd['message'], smd['data'] = True, f'Successfully retrieved all order items of user ' \
                                                                f'{user_id}', serializer.data
            return Response(data=smd, status=status.HTTP_200_OK)
        except Exception:
            return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)

    # @method_decorator(logged_in)
    def post(self, request, *args, **kwargs):

        smd = {
            'success': False,
            'message': 'Unsuccessful in creating order',
            'data': []
        }
        try:
            pdb.set_trace()
            token = request.headers.get('token')
            payload = TokenService().decode_token(token)
            user_id = payload.get('id')
            serializer = OrderProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(customer_id=user_id)
                ordered_product = OrderProduct.objects.get(customer_id=user_id, product_id=serializer.validated_data.get('product'),
                                                           is_billed=False)
                if Cart.objects.filter(customer_id=user_id, order_placed=False).exists() is True:
                    cart = Cart.objects.get(customer_id=user_id, order_placed=False)
                    cart.items.add(ordered_product)
                    cart.save()
                else:
                    user = User.objects.get(pk=user_id)
                    cart = Cart(customer=user, order_placed=False, total_amount=ordered_product.subtotal)
                    cart.save()
                    cart.items.add(ordered_product)
                smd['success'], smd['message'] = True, 'Successfully created Order Item'
                return Response(data=smd, status=status.HTTP_200_OK)
            else:
                smd['data'] = serializer.errors
                return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # smd['data'] =
            return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)


class OrderOperationsView(GenericAPIView):

    @method_decorator(logged_in)
    def patch(self, request, *args, **kwargs):
        smd = {
            'success': False,
            'message': f'Unsuccessful in updating product',
            'data': []
        }

        try:
            # pdb.set_trace()
            serializer = OrderProductSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                order = OrderProduct.objects.get(pk=args[1].get('id'))
                serializer.update(order, serializer.validated_data)
                smd['success'], smd['message'] = True, f"Successfully updated order with id : {args[1].get('id')}"
                return Response(data=smd, status=status.HTTP_200_OK)
        except Exception as e:
            pass

    @method_decorator(logged_in)
    def delete(self, request, *args, **kwargs):

        pdb.set_trace()
        id = args[1].get('id')
        smd = {
            'success': False,
            'message': f'Unsuccessful in deleting order with ID : {id}'
        }

        try:
            OrderProduct.objects.get(pk=id).delete()
            smd['success'], smd['message'] = True, f'Successfully deleted order with id : {id}'
            return Response(data=smd, status=status.HTTP_200_OK)
        except Exception as e:
            pass
