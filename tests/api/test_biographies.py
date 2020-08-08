from django.urls import reverse

from havel_backend.apps.biographies.models import Biography
from havel_backend.apps.tags.models import Tag
from tests import TestCase


class BiographyAPITest(TestCase):

    def test_index(self):
        biography = Biography.objects.create(
            title='First banner',
            image=self.get_file(),
            position=1,
            description='# Description',
            short_description='Short description',
        )

        # hit api galeries index
        response = self.client.get(reverse('api:biographies:index'), **self.headers)
        biography_data = response.json()['biographies']

        self.assertEqual(biography.title, biography_data[0]['title'])
        self.assertEqual(biography.short_description, biography_data[0]['short_description'])
        self.assertEqual(biography.position, biography_data[0]['position'])
        self.assertEqual(biography.image.url, biography_data[0]['image_url'])
        self.assertEqual([], biography_data[0]['tag_ids'])

        tag_data = response.json()['tags']
        self.assertEqual(len(tag_data), 0)

        tag = Tag.objects.create(name='Education')
        tag.biographies.add(biography)

        response = self.client.get(reverse('api:biographies:index'), **self.headers)
        biography_data = response.json()['biographies']
        self.assertEqual([tag.id], biography_data[0]['tag_ids'])

        tag_data = response.json()['tags']
        self.assertEqual(len(tag_data), 1)
        self.assertEqual(tag.name, tag_data[0]['name'])
