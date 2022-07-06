from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _
from embed_video.fields import EmbedVideoField


class GalleryModel(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('title'))
    short_descriptions = RichTextUploadingField(verbose_name=_('short_description'))
    long_descriptions = RichTextUploadingField(verbose_name=_('long_description'))
    last_date = models.DateField(null=True, verbose_name=_('last_date'))
    video = EmbedVideoField(null=True, verbose_name=_('video'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')


class GalleyImageModel(models.Model):
    product = models.ForeignKey(GalleryModel, on_delete=models.CASCADE, related_name='images',
                                verbose_name=_('gallery'), null=True, blank=True)
    image = models.ImageField(upload_to='gallery_images', verbose_name=_('image'), null=True, blank=True)

    class Meta:
        verbose_name = _('gallery image')
        verbose_name_plural = _('gallery images')
