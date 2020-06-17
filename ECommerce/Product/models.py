from django.db import models
from Users.models import User

# Create your models here.


class Product(models.Model):  # Product Inventory which only admin can access

    name = models.CharField(max_length=32, blank=False)
    images = models.URLField(max_length=2048, blank=True, null=True)
    quantity = models.CharField(max_length=6, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.name


class OrderProduct(models.Model):  # Each product is linked to a particular customer/userID.

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=2, blank=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    is_billed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk}'

    def get_subtotal(self):
        return self.product.price * self.quantity
