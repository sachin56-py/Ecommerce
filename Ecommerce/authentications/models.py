from django.db import models
from django.contrib.auth.models import User
from products.models import BaseModel

# Create your models here.
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to="profile")


class userDetails(BaseModel):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
     

