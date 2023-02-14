from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from embed_video.fields import EmbedVideoField


class AboutModel(models.Model):
    title = models.TextField(max_length=90, verbose_name=_('title'))
    image = models.FileField(upload_to='about', verbose_name=_('image'))
    description = models.TextField(verbose_name=_('description'))
    url = EmbedVideoField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return strip_tags(self.title)

    def get_absolute_url(self):
        return reverse('home:about',)
    # def get_absolute_url(self):
    #     return f'/{self.title}'

    class Meta:
        verbose_name = _('about')
        verbose_name_plural = _('abouts')
        ordering = ['-pk']


class RequestsModel(models.Model):
    name = models.CharField(max_length=90, verbose_name=_('name'))
    phone = models.CharField(max_length=20, verbose_name=_('phone'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('call center')
        verbose_name_plural = _('call center')


