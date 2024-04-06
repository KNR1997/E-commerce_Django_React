from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, related_name='products_created', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='products_updated', on_delete=models.CASCADE, null=True, blank=True)

class Order(models.Model):
    order_number = models.CharField(max_length=100)
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='orders_created', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, related_name='orders_updated', on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(default=timezone.now)
