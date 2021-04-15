from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('questions', views.questions, name="questions"),
    path('update_type_professional', views.update_type_professional, name="update_type_professional"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
