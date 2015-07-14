from cinemair.common.api import viewsets

from . import serializers
from . import services


class MoviesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.MovieSerializer
    queryset = services.get_all_movies()
