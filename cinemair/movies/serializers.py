from cinemair.common.api import serializers

from  . import models


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie


class MovieRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
