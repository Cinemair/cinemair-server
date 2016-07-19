from cinemair.common.api import viewsets
from cinemair.common.api import permissions

from . import serializers
from . import services


class CinemasViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CinemaSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return services.get_all_cinemas()

