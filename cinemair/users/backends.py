"""
Authentication backends for rest framework.

This module exposes two backends: session and token.

The first (session) is a modified version of standard
session authentication backend of restframework with
csrf token disabled.

And the second (token) implements own version of oauth2
like authentiacation but with selfcontained tokens. Thats
makes authentication totally stateles.

It uses django signing framework for create new
selfcontained tokens. This trust tokes from external
fraudulent modifications.
"""

import re

from django.conf import settings
from rest_framework.authentication import BaseAuthentication

from .token import get_user_for_token


class Session(BaseAuthentication):
    """
    Session based authentication like the standard
    `taiga.base.api.authentication.SessionAuthentication`
    but with csrf disabled (for obvious reasons because
    it is for api.

    NOTE: this is only for api web interface. Is not used
    for common api usage and should be disabled on production.
    """

    def authenticate(self, request):
        http_request = request._request
        user = getattr(http_request, 'user', None)

        if not user or not user.is_active:
            return None

        return (user, None)


class Token(BaseAuthentication):
    """
    Self-contained stateles authentication implementatrion
    that work similar to oauth2.
    It uses django signing framework for trust data stored
    in the token.
    """

    auth_rx = re.compile(r"^Bearer (.+)$")

    def authenticate(self, request):
        if "HTTP_AUTHORIZATION" not in request.META:
            return None

        token_rx_match = self.auth_rx.search(request.META["HTTP_AUTHORIZATION"])
        if not token_rx_match:
            return None

        token = token_rx_match.group(1)
        max_age_auth_token = getattr(settings, "MAX_AGE_AUTH_TOKEN", None)
        user = get_user_for_token(token, "authentication",
                                  max_age=max_age_auth_token)

        return (user, token)

    def authenticate_header(self, request):
        return 'Bearer realm="api"'
