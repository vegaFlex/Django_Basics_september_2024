from django.contrib import admin

from petstagram.pets import models


@admin.register(models.Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
