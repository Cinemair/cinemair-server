from cinemair.common.api import viewsets
from cinemair.common.api import mixins

from . import serializers
from . import services
from . import models


class ShowsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ShowSerializer
    queryset = services.get_all_shows()

class ShowsNestedViewSet(mixins.NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    queryset = services.get_all_shows()

class CinemaShowsNestedViewSet(ShowsNestedViewSet):
    serializer_class = serializers.CinemaShowNestedSerializer

class FilmShowsNestedViewSet(ShowsNestedViewSet):
    serializer_class = serializers.FilmShowNestedSerializer

