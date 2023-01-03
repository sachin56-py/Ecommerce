from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)  # will add date and time when it is created
    updated_at = models.DateTimeField(auto_now_add=True) # will add date and time when it is updated

    class Meta:   # we don not want django to make a model from here but only to act as a class
        abstract = True



class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to="categories")



class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    price = models.IntegerField()
    product_description = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)



class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(upload_to="product")
