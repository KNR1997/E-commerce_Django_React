from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=20)
    language = models.CharField(max_length=10)
    slug = models.CharField(max_length=20)
    banners = models.JSONField(default=list)
    promotional_sliders = models.JSONField(default=list)
    settings = models.JSONField(default=dict)
    icon = models.CharField(max_length=20, default='default_icon') 
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, default='default-slug')  # Add this field
    description = models.TextField()  # Modify to TextField to accommodate longer descriptions
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.URLField(default='https://picsum.photos/id/1/200/300')  # Add this field
    gallery = models.JSONField(default=list)  # Add this field
    created_by = models.ForeignKey(User, related_name='products_created', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='products_updated', on_delete=models.CASCADE, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default=None)  # Add this field
    status = models.CharField(max_length=20, default='publish')  # Add status field with default value
    product_type = models.CharField(max_length=20, default='simple')
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    order_number = models.CharField(max_length=100)
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, default="product_name")
    status = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='orders_created', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, related_name='orders_updated', on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(default=timezone.now)
