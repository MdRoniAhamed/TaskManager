from django.contrib import admin
from .models import Task,Image

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user','title','description','priority','complete','update_date']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','task','image']
