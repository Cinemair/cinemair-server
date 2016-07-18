from django.contrib import admin

from . import models

class EventsInline(admin.TabularInline):
    model = models.Event
    extra = 0
