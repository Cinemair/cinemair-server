from rest_framework import serializers as drf_serializers

from cinemair.common.api import serializers
from cinemair.cinemas.serializers import CinemaRelatedSerializer
from cinemair.films.serializers import FilmRelatedSerializer

from  . import models


class ShowSerializer(serializers.ModelSerializer):
    film_info = drf_serializers.SerializerMethodField()
    cinema_info = drf_serializers.SerializerMethodField()

    class Meta:
        model = models.Show

    def get_film_info(self, obj):
        data = FilmRelatedSerializer(obj.film).data
        del data["id"]
        return data

    def get_cinema_info(self, obj):
        data = CinemaRelatedSerializer(obj.cinema).data
        del data["id"]
        return data
