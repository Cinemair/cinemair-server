from django.contrib import admin

from . import models


class ShowsInline(admin.TabularInline):
    model = models.Show
    extra = 0
