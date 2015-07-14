from rest_framework import serializers



class JsonField(serializers.Field):
    """
    Json objects serializer field.
    """
    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        return data


class Serializer(serializers.Serializer):
    pass


class ModelSerializer(serializers.ModelSerializer):
    pass
