from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Person)
admin.site.register(Country)
admin.site.register(Pet)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Language, LanguageAdmin)
