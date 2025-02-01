from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, timedelta
from django.contrib import admin

# Create your models here.

def get_due_date():
    return datetime.now() + timedelta(days=7)

class Product(models.Model):
    VOLUME_CHOICES = [
        ('50ml', '50ml'),
        ('100ml', '100ml'),
    ]
    GENDER = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Unisex', 'Unisex'),
    ]
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER)
    description = models.TextField(default=None, null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(50)]  # Price must be at least 50
    )
    volume = models.CharField(max_length=5, choices=VOLUME_CHOICES)
    in_stock = models.BooleanField(default=False)
    stock_quantity = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]  # Stock quantity must be at least 0
    )
    on_sale = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        null=True, 
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(100)]  # Discount percentage must be between 1 and 100
    )
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.discount_percentage:
            self.discount_price = self.price - (self.price * self.discount_percentage / 100)
        else:
            self.discount_price = self.price
        super(Product, self).save(*args, **kwargs)

    def clean(self):
        """Override the clean method to ensure stock_quantity does not go below 0"""
        if self.stock_quantity < 0:
            raise ValidationError({'stock_quantity': 'Stock quantity cannot be less than 0.'})

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField(default=get_due_date)

    def __str__(self):
        return self.title

class Order(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name