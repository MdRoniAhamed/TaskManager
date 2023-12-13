from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# from datetime import *
# Priority Choice 
from django.utils import timezone
CHOICE = (
    ('low','Low'),
    ('medium','Medium'),
    ('high', 'High')
)

# Task Model 
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    start_date = models.DateTimeField(default=timezone.now,blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=50,choices=CHOICE)
    complete = models.BooleanField(default=False,blank=True,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class Image(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='Task')

    def __str__(self) -> str:
        return f"{self.task.title}"
