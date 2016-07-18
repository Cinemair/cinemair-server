from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from requests.exceptions import HTTPError

import tmdbsimple as tmdb



if not hasattr(settings, "THEMOVIEDB_API_KEY"):
    raise ImproperlyConfigured("Yoy need to a API Key of TheMovieDB.com to use its API.")

tmdb.API_KEY = settings.THEMOVIEDB_API_KEY

LANG_CODE = getattr(settings, "THEMOVIEDB_LANG_CODE", None)


def movie_info(id):
    info = {}
    info2 = {}

    try:
        info = tmdb.Movies(id).info()
    except HTTPError:
        return None

    if LANG_CODE:
        try:
            info2 = tmdb.Movies(id).info(language=LANG_CODE)
        except HTTPError:
            return info

    return {**info, **info2}


def movie_videos(id):
    info = []
    info2 = []

    try:
        info = tmdb.Movies(id).videos().get("results", [])
    except HTTPError:
        return None

    if LANG_CODE:
        try:
            info2 = tmdb.Movies(id).videos(language=LANG_CODE).get("results", [])
        except HTTPError:
            return info

    return info2 or info
