from django.contrib import admin
from .models import Product
# Register your models here.
class MuseumAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    list_display_links = ('name',)
    list_per_page = 25

admin.site.register(Product, MuseumAdmin)
