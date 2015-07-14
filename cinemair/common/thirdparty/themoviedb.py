from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from requests.exceptions import HTTPError

import tmdbsimple as tmdb



if not hasattr(settings, "THEMOVIEDB_API_KEY"):
    raise ImproperlyConfigured("Yoy need to a API Key of TheMovieDB.com to use its API.")

tmdb.API_KEY = settings.THEMOVIEDB_API_KEY



def movie_info(id):
    try:
        return tmdb.Movies(id).info()
    except HTTPError:
        return None
