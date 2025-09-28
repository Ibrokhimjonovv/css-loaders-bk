from django.contrib import admin
from .models import Loader

@admin.register(Loader)
class LoaderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'group_id', 'is_light', 'created_at')
