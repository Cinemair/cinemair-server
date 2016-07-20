from rest_framework import serializers as drf_serializers

from cinemair.common.api import serializers
from cinemair.shows.serializers import ShowRelatedSerializer

from  . import models


class FavoriteSerializer(serializers.ModelSerializer):
    show_info = drf_serializers.SerializerMethodField()

    class Meta:
        model = models.Favorite

    def get_show_info(self, obj):
        data = ShowRelatedSerializer(obj.show).data
        del data["id"]
        return data

    def validate_user(self, value):
        """
        Check that the user is the same as request.user.
        """
        if "request" in self.context:
            current_user = self.context["request"].user

            if current_user != value:
                raise drf_serializers.ValidationError("User must be you.")
        return value
