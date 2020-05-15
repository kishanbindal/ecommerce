from rest_framework.serializers import ModelSerializer
from .models import User


class LoginOtpViewSerializer(ModelSerializer):

    class Meta:

        model = User
        fields = ['phone_number']
