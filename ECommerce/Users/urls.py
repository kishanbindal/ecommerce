from django.urls import path, include
from . import views

urlpatterns = [
    path('api/login', views.LoginOtp.as_view(), name="login-otp-generation"),
    path('api/login-submit', views.LoginUser.as_view(), name="login-otp"),
]
