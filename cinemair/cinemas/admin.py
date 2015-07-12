from django.contrib import admin

from cinemair.shows.admin import ShowsInline

from . import models


@admin.register(models.Cinema)
class Cinemas(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("name",)}),
    )
    inlines = [ShowsInline,]
    list_display = ("id", "name",)
    #list_filter = (,)
    search_fields = ("name",)
    ordering = ("name",)
