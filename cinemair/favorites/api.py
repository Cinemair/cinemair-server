from cinemair.common.api import viewsets
from cinemair.common.api import permissions

from . import serializers
from . import services


class FavoritesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FavoriteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return services.get_all_upcoming_favorites().filter(user=self.request.user)
