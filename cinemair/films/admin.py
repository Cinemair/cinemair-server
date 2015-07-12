from django.contrib import admin

from cinemair.shows.admin import ShowsInline

from . import models


@admin.register(models.Film)
class Films(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("name",)}),
    )
    inlines = [ShowsInline,]
    list_display = ("id", "name",)
    #list_filter = (,)
    search_fields = ("name",)
    ordering = ("name",)