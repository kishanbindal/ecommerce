from rest_framework.serializers import ModelSerializer
from .models import Cart


class CartViewSerializer(ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"
