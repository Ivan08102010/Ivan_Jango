import django.utils.timezone
from django.db import models


class Status(models.IntegerChoices):
    Draft = 0, 'не интересно'
    INTERESTING = 1, 'интересно'

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    ispublished = models.BooleanField(default=True)


class Pupil(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True)
    year_old = models.IntegerField(default=10)
    class_p = models.CharField(max_length=3)
    gender = models.CharField(max_length=1, default='м')
    bithday = models.DateTimeField(blank=True)
    coming_of_age = models.BooleanField(default=True)


class Like_Books(models.Model):
    name = models.CharField(default='Имя книги', max_length=30,verbose_name='Имя')
    summary = models.CharField(default='Краткое содержание', max_length=100000,verbose_name='Кратко')
    Author = models.CharField(default='Автор',max_length=50,verbose_name='Автор')
    date_born_author = models.DateTimeField(max_length=1,verbose_name='Дата рождения автора')
    date_create = models.DateTimeField(max_length=1,verbose_name='Дата создания книги')
    interesting = models.BooleanField(choices=tuple(lambda x:(bool(x[0],x[1]),Status.choices)),verbose_name='Интересная ли книга')
    Genre = models.CharField(default='Жанр',max_length=12,verbose_name='Жанр')
    size = models.FloatField(default='размер',max_length=7,verbose_name='Размер')
    class Meta:
        verbose_name = 'любимые книги'
        verbose_name_plural = 'любимые книги'

# Create your models here.


# python manage.py makemigrations
# python manage.py migrate
# python manage.py sqlmigrate women 0003


# python manage.py shell_plus
