from django.utils import timezone

from .models import Event


def get_all_events():
    return (Event.objects.select_related('user',
                                        "show",
                                        "show__cinema",
                                        "show__movie")
                        .filter(show__datetime__gte=timezone.now())
                        .order_by("show__datetime", "show__cinema", "show__id"))
