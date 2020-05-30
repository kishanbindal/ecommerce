from django.db import models
from Users.models import User

# Create your models here.


class Product(models.Model):  # Product Inventory which only admin can access

    name = models.CharField(max_length=32, blank=False)
    images = models.URLField(blank=True, null=True)
    quantity = models.CharField(max_length=6, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.name


class Cart(models.Model):  # Each product is linked to a particular customer/userID.

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    quantity = models.CharField(max_length=2, blank=False)
    subtotal = models.DecimalField(max_digits=7, decimal_places=2)
    is_billed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk}'
