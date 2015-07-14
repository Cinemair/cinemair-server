from cinemair.common.api import serializers

from  . import models


class MovieSerializer(serializers.ModelSerializer):
    tmdb_info = serializers.JsonField()

    class Meta:
        model = models.Movie


class MovieRelatedSerializer(MovieSerializer):
    pass
