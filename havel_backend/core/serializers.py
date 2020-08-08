from havel_backend.apps.galeries.models import Galery
from havel_backend.apps.biographies.models import Biography
from havel_backend.apps.tags.models import Tag


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


def serialize_biography(biography: Biography) -> dict:
    return {
        'id': biography.id,
        'image_url': biography.image.url,
        'title': biography.title,
        'description': biography.description,
        'url_target': biography.url_target,
        'short_description': biography.short_description,
        'position': biography.position,
        'created': int(biography.created.timestamp()),
        'tag_ids': [tag.id for tag in biography.tags.all()]
    }


def serialize_tag(tag: Tag) -> dict:
    return {
        'id': tag.id,
        'name': tag.name
    }
