from cinemair.common.api import viewsets
from cinemair.common.api import mixins
from cinemair.common.api import permissions

from . import serializers
from . import services
from . import models


class ShowsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ShowSerializer
    queryset = services.get_all_upcoming_shows()
    permission_classes = (permissions.IsAuthenticated,)

class ShowsNestedViewSet(mixins.NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = services.get_all_upcoming_shows()

class CinemaShowsNestedViewSet(ShowsNestedViewSet):
    serializer_class = serializers.CinemaShowNestedSerializer

class MovieShowsNestedViewSet(ShowsNestedViewSet):
    serializer_class = serializers.MovieShowNestedSerializer

