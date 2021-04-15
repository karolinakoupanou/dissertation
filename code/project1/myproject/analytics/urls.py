from django.urls import path
from . import views

urlpatterns = [
    path('update_counter_more', views.update_counter_more, name='update_counter_more'),
    path('update_counter_readmore', views.update_counter_readmore, name='update_counter_readmore'),
    path('update_counter_video', views.update_counter_video, name='update_counter_video'),
    path('update_counter_playedvideo', views.update_counter_playedvideo, name='update_counter_playedvideo'),
    path('classify/',views.call_model, name ='call_model')
]
