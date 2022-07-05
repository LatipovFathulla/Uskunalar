from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _


class GalleryModel(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('title'))
    short_descriptions = RichTextUploadingField(verbose_name=_('short_description'))
    image = models.FileField(upload_to='gallery_image', verbose_name=_('image'))
    long_descriptions = RichTextUploadingField(verbose_name=_('long_description'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')

