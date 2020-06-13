from django.contrib.auth import get_user_model
from django.db import models
from Product.models import OrderProduct
from Users.models import User

# Create your models here.


class Cart(models.Model):

    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderProduct)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=256, blank=True)
    order_placed = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.first_name + " " + self.customer.last_name

    # def _calculate_total(self):
    #     total = 0
    #     for item in self.items.all():
    #         total += item.subtotal
    #     return total

