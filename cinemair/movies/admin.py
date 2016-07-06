import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import HtmlFormatter
from django.utils.safestring import mark_safe

from django.contrib import admin
from cinemair.shows.admin import ShowsInline

from . import models


def _render_pretty_json_field(instance, fieldname):
    """Function to display pretty version of our data"""
    data = getattr(instance, fieldname, "null")
    # Convert the data to sorted, indented JSON
    response = json.dumps(data, sort_keys=True, indent=2)
    # Get the Pygments formatter
    formatter = HtmlFormatter(style="colorful", prestyles="white-space: pre-wrap;")
    # Highlight the data
    response = highlight(response, JsonLexer(), formatter)
    # Get the stylesheet
    style = "<style>{}</style><br>".format(formatter.get_style_defs())
    # Safe the output
    return mark_safe(style + response)


@admin.register(models.Movie)
class Movies(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("name", "tmdb_id")}),
        ("The MovieDB info", {"fields": ("pretty_tmdb_info", "pretty_tmdb_videos"),
                              "classes": ("collapse","wide",)}),
    )
    readonly_fields = ("pretty_tmdb_info", "pretty_tmdb_videos")
    inlines = [ShowsInline,]
    list_display = ("id", "name", "tmdb_id")
    #list_filter = (,)
    search_fields = ("name",)
    ordering = ("name",)

    def pretty_tmdb_info(self, instance):
        return _render_pretty_json_field(instance, "tmdb_info")

    pretty_tmdb_info.short_description = 'TMDB info'

    def pretty_tmdb_videos(self, instance):
        return _render_pretty_json_field(instance, "tmdb_videos")

    pretty_tmdb_videos.short_description = 'TMDB videos'
