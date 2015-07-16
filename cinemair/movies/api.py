from cinemair.common.api import viewsets
from cinemair.common.api import permissions

from . import serializers
from . import services


class MoviesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.MovieSerializer
    queryset = services.get_all_movies()
    permission_classes = (permissions.IsAuthenticated,)
