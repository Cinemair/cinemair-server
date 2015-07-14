from .models import Show


def get_all_shows():
    return Show.objects.select_related('cinema', "movie").all()
