from cinemair.common.api import serializers

from  . import models


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Film
