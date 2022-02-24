from django.db import models
from django.utils.translation import gettext_lazy as _


class AboutModel(models.Model):
    title = models.CharField(max_length=90, verbose_name=_('title'))
    image = models.ImageField(upload_to='about', verbose_name=_('image'))
    description = models.TextField(verbose_name=_('description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('about')
        verbose_name_plural = _('abouts')


class RequestsModel(models.Model):
    name = models.CharField(max_length=90, verbose_name=_('name'))
    phone = models.CharField(max_length=20, verbose_name=_('phone'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Request')
        verbose_name_plural = _('Requests')


