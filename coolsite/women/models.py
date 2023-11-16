from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    ispublished = models.BooleanField(default=True)

class Pupil(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30,blank=True)
    year_old = models.IntegerField(default=10)
    class_p = models.CharField(max_length=3)
    gender = models.CharField(max_length=1, default='м')

# Create your models here.

#python manage.py sqlmigrate women 0003
