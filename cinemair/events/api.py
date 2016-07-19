from cinemair.common.api import viewsets
from cinemair.common.api import permissions

from . import serializers
from . import services


class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EventSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return services.get_all_upcoming_events().filter(user=self.request.user)
