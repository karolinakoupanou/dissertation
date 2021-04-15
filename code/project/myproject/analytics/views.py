from django.shortcuts import render,get_object_or_404
from .models import Session
from django.http import HttpResponse
from .apps import AnalyticsConfig
from django.http import JsonResponse
from rest_framework.views import APIView
from categories.models import Category
import numpy as np

#Interactive data
# Update the counter_more field of Session database and call the model each time the more button is pressed in a Session except from the first time.
def update_counter_more(request):
    username = request.user.username
    queryset = Session.objects.filter(username=username,done=False)
    counter = get_object_or_404(queryset)
    counter.more_counter += 1
    counter.save()
    if counter.more_counter > 0:
        call_model(username)
    return HttpResponse("Success!")
# Update the counter_readmore field of Session database.
def update_counter_readmore(request):
    username = request.user.username
    queryset = Session.objects.filter(username=username,done=False)
    counter = get_object_or_404(queryset)
    counter.readmore_counter += 1
    counter.save()
    return HttpResponse("Success!")
# Update the counter_video field of Session database.
def update_counter_video(request):
    username = request.user.username
    queryset = Session.objects.filter(username=username,done=False)
    counter = get_object_or_404(queryset)
    counter.video_counter += 1
    counter.save()
    return HttpResponse("Success!")
# Update the counter_playedvideo field of Session database.
def update_counter_playedvideo(request):
    username = request.user.username
    queryset = Session.objects.filter(username=username,done=False)
    counter = get_object_or_404(queryset)
    counter.played_videos += 1
    counter.save()
    return HttpResponse("Success!")
# Update the counter_links field of Session database.
def update_counter_links(request):
    username = request.user.username
    queryset = Session.objects.filter(username=username,done=False)
    counter = get_object_or_404(queryset)
    counter.links_counter += 1
    counter.save()
    return HttpResponse("Success!")
#When the model is called the interactive data of the user until this point are used to enable the model to predict the persona and update it to the Category database.
def call_model(current_username):
    queryset = Session.objects.filter(username=current_username)
    counter = get_object_or_404(queryset)
    x_data = [[counter.more_counter,counter.readmore_counter,counter.video_counter,counter.played_videos,counter.links_counter]]
    prediction = AnalyticsConfig.gnb.predict(x_data)
    queryset = Category.objects.filter(username=current_username)
    queryset2 = get_object_or_404(queryset)
    queryset2.type =''.join(prediction)
    queryset2.verified = True
    queryset2.save()
    return HttpResponse("Success!")

