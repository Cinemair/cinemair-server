from cinemair.common.api import viewsets

from . import serializers
from . import services


class FilmsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.FilmSerializer
    queryset = services.get_all_films()
