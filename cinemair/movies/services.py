from .models import Movie


def get_all_movies():
    return Movie.objects.all().order_by("name")
