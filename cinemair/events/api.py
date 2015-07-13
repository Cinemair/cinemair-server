from cinemair.common.api import viewsets

from . import serializers
from . import services


class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EventSerializer
    queryset = services.get_all_events()

