from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication


class JSONSingleTokenAuthentication(TokenAuthentication):

    token = 'CyzOdMKGPLoUpTjGjvDyjjLP6mIVrw6Kfnvej5LK2w3J2XGGBz'

    def authenticate(self, request):
        token = super().authenticate(request)

        if not token:
            raise exceptions.AuthenticationFailed("Invalid token header. No credentials provided.")

    def authenticate_credentials(self, key):

        if key != self.token:
            raise exceptions.AuthenticationFailed('Invalid Token')

        return key
