from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from embed_video.fields import EmbedVideoField


class GalleryModel(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('title'), null=True,)
    short_descriptions = RichTextUploadingField(verbose_name=_('short_description'), null=True,)
    long_descriptions = RichTextUploadingField(verbose_name=_('long_description'), null=True,)
    last_date = models.DateField(null=True, verbose_name=_('last_date'), blank=True)
    video = EmbedVideoField(null=True, verbose_name=_('video'), blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')


class GalleyImageModel(models.Model):
    product = models.ForeignKey(GalleryModel, on_delete=models.CASCADE, related_name='images',
                                verbose_name=_('gallery'), null=True, blank=True)

    image = models.FileField(upload_to='gallery_images', verbose_name=_('image'), null=True, blank=True)

    class Meta:
        verbose_name = _('gallery image')
        verbose_name_plural = _('gallery images')
