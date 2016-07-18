from django.db.models import Count, Case, When, IntegerField
from django.utils import timezone

from .models import Movie


def get_all_upcoming_movies():
    return (Movie.objects.annotate(remained_shows=Count(Case(
                                When(shows__datetime__gte=timezone.now(), then=1),
                                output_field=IntegerField())))
                         .filter(remained_shows__gt=0)
                         .order_by("name"))
