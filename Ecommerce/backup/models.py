from django.db import models
import uuid


# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)  # will add date and time when it is created
    updated_at = models.DateTimeField(auto_now=True) # will add date and time when it is updated

    class Meta:   # we don not want django to make a model from here but only to act as a class
        abstract = True