from rest_framework import serializers as drf_serializers

from cinemair.common.api import serializers
from cinemair.cinemas.serializers import CinemaRelatedSerializer
from cinemair.movies.serializers import MovieRelatedSerializer

from  . import models


class ShowSerializer(serializers.ModelSerializer):
    movie_info = drf_serializers.SerializerMethodField()
    cinema_info = drf_serializers.SerializerMethodField()
    event = drf_serializers.SerializerMethodField()

    class Meta:
        model = models.Show

    def get_movie_info(self, obj):
        data = MovieRelatedSerializer(obj.movie).data
        del data["id"]
        return data

    def get_cinema_info(self, obj):
        data = CinemaRelatedSerializer(obj.cinema).data
        del data["id"]
        return data

    def get_event(self, obj):
        try:
            return obj.events.get(user=self.context['request'].user).id
        except:
            return None



class ShowRelatedSerializer(ShowSerializer):
    pass


class CinemaShowNestedSerializer(ShowSerializer):
    class Meta(ShowSerializer.Meta):
        exclude = ("cinema_info",)


class MovieShowNestedSerializer(ShowSerializer):
    class Meta(ShowSerializer.Meta):
        exclude = ("movie_info",)
