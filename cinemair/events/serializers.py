from rest_framework import serializers as drf_serializers

from cinemair.common.api import serializers
from cinemair.shows.serializers import ShowRelatedSerializer

from  . import models


class EventSerializer(serializers.ModelSerializer):
    show_info = drf_serializers.SerializerMethodField()

    class Meta:
        model = models.Event

    def get_show_info(self, obj):
        data = ShowRelatedSerializer(obj.show).data
        del data["id"]
        return data
