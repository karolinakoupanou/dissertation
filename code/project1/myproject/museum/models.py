
from django.db import models
#from django.db.models import Model
from django.conf import settings
from stdimage import StdImageField, JPEGField
from django.contrib.postgres.fields import HStoreField

class Product(models.Model):
    name = models.CharField(max_length=200)
    text_description = models.CharField(max_length=200,default=None)
    more_info = models.CharField(max_length=2000,default=None)
    product_image = models.ImageField(upload_to ='uploads/',default=None)
    video = models.FileField(upload_to ='uploads/',default=None)
    link_1 = models.URLField(max_length=200,default=None)
    link_2 = models.URLField(max_length=200,default=None)

def __str__(self):
    return self.id
