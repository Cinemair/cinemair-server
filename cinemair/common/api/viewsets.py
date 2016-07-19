from rest_framework import viewsets
from rest_framework import mixins


class GenericViewSet(viewsets.GenericViewSet):
    """
    The GenericViewSet class does not provide any actions by default,
    but does include the base set of generic view behavior, such as
    the `get_object` and `get_queryset` methods.
    """
    def get_serializer_context(self):
        return {'request': self.request}


class ModelViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    def get_serializer_context(self):
        return {'request': self.request}


class ReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides default `list()` and `retrieve()` actions.
    """
    def get_serializer_context(self):
        return {'request': self.request}


class CreateModelViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Create objects mixin
    """
    def get_serializer_context(self):
        return {'request': self.request}
