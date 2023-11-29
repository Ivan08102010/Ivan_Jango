import django.utils.timezone
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
    bithday = models.DateTimeField(default= django.utils.timezone.now())
    coming_of_age = models.BooleanField(default = True)

class Like_Books(models.Model):
    name_Book = models.CharField(default= 'Book',max_length=30)
    summary = models.CharField(default='Жили были и стали жить поживать да добра наживать',max_length=200)
    Author = models.CharField(max_length=20)
    date_born_author = models.DateTimeField(max_length=1)
    date_create = models.DateTimeField(max_length=1)
    interesting = models.BooleanField(default = True)
    Genre = models.CharField(max_length=12)
    size = models.FloatField(max_length=7)



# Create your models here.

#python manage.py makemigrations
#python manage.py migrate
#python manage.py sqlmigrate women 0003
