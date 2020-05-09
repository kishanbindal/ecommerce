from django.test import Client, RequestFactory
from django.urls import reverse
from services.sms_service import OtpService, SmsService
from services.redis_service import Redis
from Users import views, models
import fakeredis
import pdb
import pytest
from unittest import mock


otp_service = OtpService()
User = models.UserInfo
connection = fakeredis.FakeStrictRedis()


@pytest.mark.django_db
class TestLoginOtpGenerationFunctionality:

    @pytest.fixture()
    def set_up(self):

        User.objects.create(first_name="Kishan", last_name="Bindal", phone_number="+911234567800")

    def test_check_user_exists_return_200(self, set_up):
        phone_number = '+911234567800'
        path = reverse('login-otp-generation')
        request = RequestFactory().post(path)
        request.data = {'phone_number': phone_number}
        response = views.LoginOtp.post(self, request)
        assert response.status_code == 200

    def test_check_user_does_not_exist_return_400(self, set_up):
        phone_number = '+911234567805'
        path = reverse('login-otp-generation')
        request = RequestFactory().post(path)
        request.data = {'phone_number': phone_number}
        response = views.LoginOtp.post(self, request)
        assert response.status_code == 400

    def test_otp_length(self, set_up):
        phone_number = '+911234567800'
        path = reverse('login-otp-generation')
        request = RequestFactory().post(path)
        request.data = {
            'phone_number': phone_number
        }
        response = views.LoginOtp.post(self, request)
        otp, validity_period = otp_service.generate_otp()
        otp = str(otp)
        otp_length = len(otp) == 6
        if otp_length is True:
            response_code = 200
            assert response_code == response.status_code
        else:
            response_code = 400
            assert response_code == response.status_code

    def test_correct_type_otp_return_200(self, set_up):
        phone_number = '+911234567800'
        path = reverse('login-otp-generation')
        request = RequestFactory().post(path)
        request.data = {
            'phone_number': phone_number
        }
        response = views.LoginOtp.post(self, request)
        otp, validity_period = otp_service.generate_otp()
        otp_type = type(otp)
        print('Otp type: ', otp_type)
        if otp_type is int:
            assert 200 == response.status_code

    def test_wrong_type_otp_return_400(self, set_up):
        phone_number = '+911234567800'
        path = reverse('login-otp-generation')
        request = RequestFactory().post(path)
        request.data = {
            'phone_number': phone_number
        }
        response = views.LoginOtp.post(self, request)
        otp, validity_period = otp_service.generate_otp()
        otp_type = type(otp)
        if otp_type is not int:
            assert 400 == response.status_code


@pytest.mark.django_db
class TestOtpSubmissionFunctionality:

    @pytest.fixture()
    def set_up(self):
        phone_number = '+0911234567890'
        user = User.objects.create(first_name='Kishan', last_name="Bindal", phone_number=phone_number)
        user.save()
        otp, step = otp_service.generate_otp()
        url = reverse('login-otp')
        return otp, url, phone_number

    def test_check_user_does_not_exists_return_400(self, set_up):
        otp, path, phone_number = set_up[0], set_up[1], set_up[2]
        request = RequestFactory().post(path)
        request.data = {
            'otp': otp,
            'phone_number': '+0011234567890'
        }
        response = views.LoginUser.post(self, request)
        assert response.status_code == 400

    def test_user_exists_return_200(self, set_up):
        otp, path, phone_number = set_up[0], set_up[1], set_up[2]
        request = RequestFactory().post(path)
        request.data = {
            'otp': otp,
            'phone_number': phone_number
        }
        response = views.LoginUser.post(self, request)
        assert response.status_code == 200

    def test_wrong_otp_type_return_400(self, set_up):
        path = reverse('login-otp')
        request = RequestFactory().post(path)
        request.data = {
            'otp': 'kishan',
            'phone_number': '+0911234567890'
        }
        response = views.LoginUser.post(self, request)
        if type(request.data.get('otp')) != int:
            assert response.status_code == 400

    def test_valid_otp_type_return_200(self, set_up):
        path = reverse('login-otp')
        request = RequestFactory().post(path)
        request.data = {
            'otp': 543175,
            'phone_number': set_up[2]
        }
        response = views.LoginUser.post(self, request)
        if type(request.data.get('otp')) is int:
            assert response.status_code == 200

    def test_otp_invalid_length_return_400(self, set_up):
        path = reverse('login-otp')
        phone_number = set_up[2]
        otp = 56734
        request = RequestFactory().post(path)
        request.data = {
            'otp': otp,
            'phone_number': phone_number
        }
        response = views.LoginUser.post(self, request)
        if len(str(otp)) != 6:
            assert response.status_code == 400

    def test_otp_length_return_200(self, set_up):
        otp, path, phone_number = set_up
        request = RequestFactory().post(path)
        request.data = {
            'otp': otp,
            'phone_number': phone_number
        }
        response = views.LoginUser.post(self, request)
        if len(str(otp)) == 6:
            assert response.status_code == 200

    def test_redis_cache_return_200(self, set_up):
        otp, path, phone_number = set_up[0], set_up[1], set_up[2]
        request = RequestFactory().post(path)
        request.data = {
            'otp': otp,
            'phone_number': phone_number
        }
        response = views.LoginUser.post(self, request)
        if response.status_code == 200:
            connection.set(phone_number, 'online')
            assert connection.get(phone_number).decode('utf8') == 'online'

    # @mock.patch('Users.views.rdb')
    #     # def test_redis_cache_return_200_mock(self, mock_rdb):
    #     #     pdb.set_trace()
    #     #     print(mock_rdb)
