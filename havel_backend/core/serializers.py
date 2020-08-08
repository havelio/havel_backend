from havel_backend.apps.galeries.models import Galery


def serialize_galery(galery: Galery) -> dict:
    return {
        'id': galery.id,
        'image_url': galery.image.url,
        'title': galery.title,
        'description': galery.description,
        'url_target': galery.url_target,
        'short_description': galery.short_description,
        'position': galery.position,
        'created': int(galery.created.timestamp())
    }
