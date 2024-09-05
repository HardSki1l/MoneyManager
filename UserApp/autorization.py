from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.settings import api_settings

from UserApp.models import UsersInfoModel


class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        print(auth_header)
        if not auth_header:
            raise exceptions.AuthenticationFailed('Authorization header must contain two space-delimited values')
        try:
            prefix, token = auth_header.split()
            assert prefix.lower() == 'bearer'
        except ValueError:
            raise exceptions.AuthenticationFailed('Authorization header must contain two space-delimited values')
        try:
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            raise exceptions.AuthenticationFailed(f'Token invalid: {e}')
        user_id = UntypedToken(token)['id']
        try:
            students = UsersInfoModel.objects.get(id=user_id)
        except UsersInfoModel.DoesNotExist:
            raise exceptions.AuthenticationFailed('User not found')
        return (students, None)
