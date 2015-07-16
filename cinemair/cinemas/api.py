from cinemair.common.api import viewsets
from cinemair.common.api import permissions

from . import serializers
from . import services


class CinemasViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CinemaSerializer
    queryset = services.get_all_cinemas()
    permission_classes = (permissions.IsAuthenticated,)

