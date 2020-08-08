from django.core.files import File
from django.urls import reverse

from havel_backend.apps.galeries.models import Galery
from tests import TestCase


class GaleryAPITest(TestCase):

    def test_index(self):
        file = File(open('media/tests.jpg', 'rb'))
        galery = Galery.objects.create(
            title='First banner',
            image=file,
            position=1,
            description='# Description',
            short_description='Short description',
        )

        # hit api galeries index
        response = self.client.get(reverse('api:galeries:index'), **self.headers)
        data = response.json()

        self.assertEqual(len(data), 1)
        self.assertEqual(galery.title, data[0]['title'])
        self.assertEqual(galery.short_description, data[0]['short_description'])
        self.assertEqual(galery.position, data[0]['position'])
        self.assertEqual(galery.image.url, data[0]['image_url'])
