from cinemair.common.api import viewsets
from cinemair.common.api import permissions

from . import serializers
from . import services


class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EventSerializer
    queryset = services.get_all_upcoming_events()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
