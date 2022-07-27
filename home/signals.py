from PIL import Image
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from home.models import BannerInfoModel, BannerImageModel


def image_compressor(sender, **kwargs):
    print('working...')
    if kwargs["created"]:
        with Image.open(kwargs["instance"].image.path) as photo:
            photo.save(kwargs["instance"].image.path, optimize=True, quality=20)


post_save.connect(image_compressor, sender=BannerImageModel)
