from cinemair.common.api import routers


router = routers.DefaultRouter(trailing_slash=False)

from cinemair.cinemas.api import CinemasViewSet
router.register(r"cinemas", CinemasViewSet, base_name="cinemas")

from cinemair.films.api import FilmsViewSet
router.register(r"films", FilmsViewSet, base_name="films")

from cinemair.shows.api import ShowsViewSet
router.register(r"shows", ShowsViewSet, base_name="shows")

