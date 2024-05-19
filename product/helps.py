import uuid
from django.db.models import TextChoices


class SaveMediaFiles(object):
    def category_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f'media/category/{uuid.uuid4()}.{image_extension}'

    def product_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f'media/category/{uuid.uuid4()}.{image_extension}'

    def clientcomment_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f'media/client/{uuid.uuid4()}.{image_extension}'
