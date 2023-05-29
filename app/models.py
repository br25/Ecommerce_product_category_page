from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from .choices import ProductCategory, ProductWarranty, ProductBrand


class Product(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)
    category = models.CharField(
        max_length=20,
        choices=ProductCategory.choices
    )
    brand = models.CharField(
        max_length=20,
        choices=ProductBrand.choices
    )
    warranty = models.CharField(
        max_length=1,
        choices=ProductWarranty.choices
    )
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='products'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_liked = models.BooleanField(default=False)


    def __str__(self):
        return self.name
