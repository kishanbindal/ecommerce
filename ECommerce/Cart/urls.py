from django.urls import path
from . import views


urlpatterns = [
    path('api/cart/', views.CartView.as_view(), name='cart')
]