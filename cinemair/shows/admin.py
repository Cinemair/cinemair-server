from django.contrib import admin

from . import models


class ShowsInline(admin.TabularInline):
    model = models.Show
    extra = 0


@admin.register(models.Show)
class Show(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("cinema", "movie", "datetime")}),
    )
    list_display = ("id", "cinema", "movie", "datetime")
    #list_editable = (,)
    list_filter = ("cinema",)
    search_fields = ("id", "cinema__name", "movie__title", "datetime")
    date_hierarchy = "datetime"
    ordering = ("cinema", "datetime")
