from cinemair.common.api import viewsets
from cinemair.common.api import mixins
from cinemair.common.api import permissions

from . import serializers
from . import services
from . import models


class ShowsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ShowSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return services.get_all_upcoming_shows()

class ShowsNestedViewSet(mixins.NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = services.get_all_upcoming_shows()
        return self._filter_queryset_by_parents_lookups(queryset)


class CinemaShowsNestedViewSet(ShowsNestedViewSet):
    serializer_class = serializers.CinemaShowNestedSerializer


class MovieShowsNestedViewSet(ShowsNestedViewSet):
    serializer_class = serializers.MovieShowNestedSerializer

