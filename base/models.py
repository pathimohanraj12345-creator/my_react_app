from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    # ... other fields like price, description, etc.

    def __str__(self):
        return self.name

class Order(models.Model):
    # ... order fields
    pass

class OrderItem(models.Model):
    # ... order item fields
    pass

class ShippingAddress(models.Model):
    # ... shipping address fields
    pass