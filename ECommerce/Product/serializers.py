from rest_framework.serializers import ModelSerializer
from .models import Product, OrderProduct


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class OrderProductSerializer(ModelSerializer):

    class Meta:
        model = OrderProduct
        exclude = ['customer']
