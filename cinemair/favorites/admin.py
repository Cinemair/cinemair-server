from django.contrib import admin

from . import models

class FavoritesInline(admin.TabularInline):
    model = models.Favorite
    extra = 0
