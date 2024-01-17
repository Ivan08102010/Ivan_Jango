from django.contrib import admin
from django.urls import path
from women.views import *

urlpatterns = [
    path('', index, name='home'),
    path('gim1/',gim1, name='gim1'),
    path('a/', a, name='a'),
    path('b/', b, name='b'),
    path('c/', c, name='c'),
    path('cats/<int:cat_id>/', categories, name='Bio'),
    path('itcube/32', itcube, name='cube'),
    path('Cats/', Cats, name='cats'),
    path('pupil/<int:p_id>/', pupil_g, name='pupil'),
    path('pupil1', pupil, name='pupil1'),
    path('book/<int:b_id>/', book_g, name='book'),
    path('books', books, name='books'),



]