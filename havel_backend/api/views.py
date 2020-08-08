from rest_framework.response import Response
from rest_framework.views import APIView as RestFrameworkView

from .authentication import JSONSingleTokenAuthentication
from .exceptions import APIError
from .permissions import IsSecure


class APIView(RestFrameworkView):
    authentication_classes = (JSONSingleTokenAuthentication,)
    permission_classes = (IsSecure,)

    def handle_exception(self, exc):
        """ Override the exception handler to handle APIError first
        """
        if isinstance(exc, APIError):
            return Response({'detail': exc.detail}, status=exc.status_code,
                            exception=True)
        return super().handle_exception(exc)
