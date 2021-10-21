from django.contrib import admin
from .models import Photo,Ask
@admin.register(Photo)
class AdminPhoto(admin.ModelAdmin):
    list_display = ("name", "date", "dir_way", "is_video")
@admin.register(Ask)
class AdminAsk(admin.ModelAdmin):
    list_display = ("name", "email", "date", "quetion")
# Register your models here.
