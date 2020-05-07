import pytest
from django.urls import resolve, reverse


class TestUserUrls:

    def testLoginWithOtpUrl(self):

        path = reverse('login-otp-generation')
        assert resolve(path).view_name == "login-otp-generation"

    def testLoginOtp(self):
        path = reverse('login-otp')
        assert resolve(path).view_name == 'login-otp'
