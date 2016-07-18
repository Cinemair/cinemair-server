from django.utils import timezone

from .models import Show


def get_all_upcoming_shows():
    return (Show.objects.select_related('cinema', "movie")
                        .prefetch_related("events")
                        .filter(datetime__gte=timezone.now())
                        .order_by("datetime", "cinema", "id"))
