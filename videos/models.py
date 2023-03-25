from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _
from embed_video.fields import EmbedVideoField


class VideoModel(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('title'))
    description = models.TextField(max_length=300, verbose_name=_('description'))
    url = EmbedVideoField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('video')
        verbose_name_plural = _('videos')