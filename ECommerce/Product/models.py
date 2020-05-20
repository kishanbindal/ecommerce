from django.db import models
from Users.models import User

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=32, blank=False)
    images = models.URLField(blank=True, null=True)
    quantity = models.CharField(blank=False)
    price = models.CharField(blank=False, null=False)

    def __str__(self):
        return self.name


class Cart(models.Model):

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total = models.DecimalField(decimal_places=2)
