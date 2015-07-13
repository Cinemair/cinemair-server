from cinemair.common.api import routers

router = routers.DefaultRouter(trailing_slash=False)


from cinemair.cinemas.api import CinemasViewSet
from cinemair.shows.api import CinemaShowsNestedViewSet
(router.register(r"cinemas", CinemasViewSet, base_name="cinemas")
       .register(r"shows", CinemaShowsNestedViewSet, base_name="cinemas-shows",
                 parents_query_lookups=["cinema"]))


from cinemair.films.api import FilmsViewSet
from cinemair.shows.api import FilmShowsNestedViewSet
(router.register(r"films", FilmsViewSet, base_name="films")
       .register(r"shows", FilmShowsNestedViewSet, base_name="films-shows",
                 parents_query_lookups=["film"]))


from cinemair.shows.api import ShowsViewSet
router.register(r"shows", ShowsViewSet, base_name="shows")


from cinemair.events.api import EventsViewSet
router.register(r"events", EventsViewSet, base_name="events")
