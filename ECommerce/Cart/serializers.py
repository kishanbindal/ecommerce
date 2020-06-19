from rest_framework.serializers import ModelSerializer
from Product.serializers import OrderSerializer
from .models import Cart


class CartViewSerializer(ModelSerializer):

    items = OrderSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = "__all__"

