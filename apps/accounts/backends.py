from django.conf import settings
from django.contrib.auth import get_user_model


class CustomUserAuth(object):

    def authenticate(self, username=None, password=None):

        if '@' in username:
            kwargs = {
                'email': username
            }
        else:
            kwargs = {
                'username': username
            }

        try:
            user = get_user_model().objects.get(**kwargs)
            if user.check_password(password):
                return user
        except get_user_model().DoesNotExist:
            return None

    def get_user(self, username):
        try:
            user = get_user_model().objects.get(pk=username)

            if user.is_active:
                return user
        except get_user_model().DoesNotExist:
            return None
