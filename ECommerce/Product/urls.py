from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.ProductsView.as_view(), name='products'),
    path('api/products/<int:id>/', views.SingleProductView.as_view(), name='product-id'),
    path('api/order/', views.OrderView.as_view(), name='order'),
    path('api/order/<int:id>', views.OrderOperationsView.as_view(), name='order-ops')
]
