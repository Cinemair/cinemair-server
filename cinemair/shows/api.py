from cinemair.common.api import viewsets

from . import serializers
from . import services


class ShowsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ShowSerializer
    queryset = services.get_all_shows()
