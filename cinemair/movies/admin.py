from django.contrib import admin

from cinemair.shows.admin import ShowsInline

from . import models


@admin.register(models.Movie)
class Movies(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("name", "tmdb_id")}),
    )
    inlines = [ShowsInline,]
    list_display = ("id", "name", "tmdb_id")
    #list_filter = (,)
    search_fields = ("name",)
    ordering = ("name",)
