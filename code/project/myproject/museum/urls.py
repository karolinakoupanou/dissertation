from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('shop', views.shop, name="shop"),
    path('<int:listing_id>', views.product_page, name="product_page"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
