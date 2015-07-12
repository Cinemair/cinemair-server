from cinemair.common.api import serializers

from  . import models


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cinema


class CinemaRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cinema
