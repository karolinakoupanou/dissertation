from django.contrib import admin
from .models import Session
from import_export.admin import ExportActionMixin

class SessionAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ('id','username','start_time')
    list_filter = ('id',)
    list_display_links = ('id',)
    list_per_page = 25

admin.site.register(Session, SessionAdmin)

# Register your models here.
