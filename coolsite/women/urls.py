from django.contrib import admin
from django.urls import path
from women.views import *

urlpatterns = [
    path('', index, name='home'),
    path('1/', d, name='123'),
    path('gim1/',gim1, name='Гимназия'),
    path('a/', a, name='1'),
    path('b/', b, name='2'),
    path('c/', c, name='3'),
    path('cats/<int:cat_id>/', categories, name='Bio')]