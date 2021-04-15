
from django.db import models
#from django.db.models import Model
from django.conf import settings


class Session(models.Model):
    username = models.CharField(max_length=200)
    start_time = models.DateTimeField(auto_now=False,auto_now_add=False)
    more_counter = models.IntegerField(default=0)
    readmore_counter = models.IntegerField(default=0)
    video_counter = models.IntegerField(default=0)
    played_videos = models.IntegerField(default=0)
    links_counter = models.IntegerField(default=0)
    end_time = models.DateTimeField(auto_now=False,auto_now_add=False)
    duration = models.CharField(max_length=300)
    done =  models.BooleanField(default=False)
def __str__(self):
    return self.id
