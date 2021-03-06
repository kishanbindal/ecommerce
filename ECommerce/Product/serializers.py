from rest_framework.serializers import ModelSerializer
from .models import Product, OrderProduct


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class OrderProductSerializer(ModelSerializer):

    # product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderProduct
        exclude = ['customer']


class OrderSerializer(ModelSerializer):

    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderProduct
        exclude = ['customer']
