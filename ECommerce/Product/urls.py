from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.ProductsView.as_view(), name='products'),
    path('api/products/<id>/', views.SingleProductView.as_view(), name='product-id'),
    path('api/cart/', views.CartView.as_view(), name='view-cart')
]
