from .models import Cinema


def get_all_cinemas():
    return Cinema.objects.all()
