from django.test import TestCase as DjangoTestCase

from havel_backend.api.authentication import JSONSingleTokenAuthentication


class TestCase(DjangoTestCase):

    headers = {
        'content_type': 'application/json',
        'wsgi.url_scheme': 'https',
        'HTTP_AUTHORIZATION': f'token {JSONSingleTokenAuthentication.token}'
    }
