from rest_framework.response import Response

from havel_backend.api.views import APIView
from havel_backend.apps.galeries.models import Galery
from havel_backend.core.serializers import serialize_galery


class Index(APIView):
    def get(self, request):
        data = [
            serialize_galery(galery) for galery in Galery.objects.all()
        ]
        return Response(data)
