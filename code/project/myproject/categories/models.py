
from django.db import models
#from django.db.models import Model
from django.conf import settings


class Category(models.Model):
    username = models.CharField(max_length=200)
    type = models.CharField(max_length=200,default=None)
    verified = models.BooleanField(default=False)

def __str__(self):
    return self.id
