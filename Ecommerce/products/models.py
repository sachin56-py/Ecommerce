from django.db import models
from backup.models import Basemodel

# Create your models here.
class Category(Basemodel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=true)
    category_image = models.ImageField(upload="categories")



class Product(Basemodel):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    price = models.IntegerField(max_length=100)
    product_description = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)



class ProductImage(Basemodel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(upload="product")
