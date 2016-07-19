from cinemair.common.api import viewsets
from cinemair.common.api import permissions

from . import serializers
from . import services


class MoviesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.MovieSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return services.get_all_upcoming_movies()
