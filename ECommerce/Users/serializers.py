from rest_framework.serializers import ModelSerializer
from .models import UserInfo


class LoginOtpViewSerializer(ModelSerializer):

    class Meta:

        model = UserInfo
        fields = ['phone_number']
