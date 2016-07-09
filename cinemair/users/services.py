from django.db import transaction as tx
from django.apps import apps
from django.conf import settings

from cinemair.users.connectors import google

from . import serializers
from . import token




def make_auth_response_data(user) -> dict:
    """
    Given a domain and user, creates data structure
    using python dict containing a representation
    of the logged user.
    """
    serializer = serializers.UserSerializer(user)
    data = dict(serializer.data)
    data["auth_token"] = token.get_token_for_user(user, "authentication")
    return data


################################
# Google Auth
################################

@tx.atomic
def google_register(username:str, email:str, full_name:str, google_id:int):
    """
    Register a new user from google.
    This can raise `exc.IntegrityError` exceptions in
    case of conflics found.
    :returns: User
    """
    user_model = apps.get_model("users", "User")

    try:
        # Google user association exist?
        user = user_model.objects.get(google_id=google_id)
    except user_model.DoesNotExist:
        try:
            # Is a user with the same email as the google user?
            user = user_model.objects.get(email=email)
            user.google_id = google_id
            user.save()
        except user_model.DoesNotExist:
            # Create a new user
            user = user_model.objects.create(email=email,
                                             username=username,
                                             full_name=full_name,
                                             google_id=google_id)

    return user


def google_login(request):
    code = request.data.get('code', None)

    user_info = google.me(code)

    user = google_register(username=user_info.username,
                           email=user_info.email,
                           full_name=user_info.full_name,
                           google_id=user_info.id)

    data = make_auth_response_data(user)
    return data
