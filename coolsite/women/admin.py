from django.contrib import admin

from women.models import Like_Books, Pupil


@admin.register(Like_Books)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id','name','Author','Genre','size','interesting')
    list_display_links = ('name',)

@admin.register(Pupil)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id','surname','name','patronymic','year_old','gender','coming_of_age')
    list_display_links = ('surname','name')
    list_editable = ('coming_of_age',)