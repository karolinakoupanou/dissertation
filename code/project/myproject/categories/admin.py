
from django.contrib import admin
from .models import Category
from import_export.admin import ExportActionMixin

class CategoryAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ('id','username','type')
    list_filter = ('id','username')
    list_display_links = ('id','username')
    list_per_page = 25

admin.site.register(Category, CategoryAdmin)

# Register your models here.
