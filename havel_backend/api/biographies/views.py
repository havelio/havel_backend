from rest_framework.response import Response

from havel_backend.api.views import APIView
from havel_backend.apps.biographies.models import Biography
from havel_backend.apps.tags.models import Tag
from havel_backend.core.serializers import serialize_biography, serialize_tag


class Index(APIView):
    def get(self, request):
        biographies = Biography.objects.all().prefetch_related('tags')
        data = {
            'biographies': [serialize_biography(biography) for biography in biographies],
            'tags': [serialize_tag(tag) for tag in Tag.objects.all()]
        }
        return Response(data)
