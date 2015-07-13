from .models import Event


def get_all_events():
    return Event.objects.select_related('user',
                                        "show",
                                        "show__cinema",
                                        "show__film").all()
