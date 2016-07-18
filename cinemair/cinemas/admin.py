from django.contrib import admin

from cinemair.shows.admin import ShowsInline

from . import models


@admin.register(models.Cinema)
class Cinemas(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("name",)}),
        ("Location", {"fields": ("address", "city", "country")}),
        ("Extra", {"fields": ("approximate_price",)}),
    )
    inlines = [ShowsInline,]
    list_display = ("id", "name", "address", "city", "country", "approximate_price")
    list_display_links = ("id", "name")
    search_fields = ("name", "address", "city", "country")
    ordering = ("name",)
