from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create =  models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    ispublished = models.BooleanField(default=True)
# Create your models here.
