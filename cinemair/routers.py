from cinemair.common.api import routers

router = routers.DefaultRouter(trailing_slash=False)


from cinemair.cinemas.api import CinemasViewSet
from cinemair.shows.api import CinemaShowsNestedViewSet
(router.register(r"cinemas", CinemasViewSet, base_name="cinemas")
       .register(r"shows", CinemaShowsNestedViewSet, base_name="cinemas-shows",
                 parents_query_lookups=["cinema"]))


from cinemair.movies.api import MoviesViewSet
from cinemair.shows.api import MovieShowsNestedViewSet
(router.register(r"movies", MoviesViewSet, base_name="movies")
       .register(r"shows", MovieShowsNestedViewSet, base_name="movies-shows",
                 parents_query_lookups=["movie"]))


from cinemair.shows.api import ShowsViewSet
router.register(r"shows", ShowsViewSet, base_name="shows")


from cinemair.events.api import EventsViewSet
router.register(r"events", EventsViewSet, base_name="events")


from cinemair.users.api import AuthViewSet
router.register(r"auth", AuthViewSet, base_name="auth")
