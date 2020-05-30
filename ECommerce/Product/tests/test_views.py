from django.contrib.auth import get_user_model
from django.test import RequestFactory
from django.urls import reverse, resolve
import pytest
from unittest import mock
from Product.models import Product, Order
import Users

User = get_user_model()
BASE_URL = '127.0.0.1/8000'


@pytest.mark.django_db
class TestProductsView:

    @pytest.fixture
    def set_up(self):
        user = User.objects.create(first_name='kishan', last_name="Bindal", phone_number="+0911234567890")
        product_1 = Product.objects.create(name="iPhone", image=None, quantity="100", price="75000")
        product_2 = Product.objects.create(name="watch", image=None, quantity="5000", price="15000")
        url = BASE_URL+"/api/login"
        # path_1 = reverse(url)  # api for getting OTP
        # request = RequestFactory().post(path_1)
        # request.data = {
        #     'phone_number': "+0911234567890"
        # }
        # response = Users.views.LoginOtp.post(self, request)
        # response.data.get('otp')
        return user, product_1, product_2

    def test_user_authenticated_return_401_if_not_authenticated(self, set_up):
        pass
