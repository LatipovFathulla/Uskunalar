from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _


class BiznesModel(models.Model):
    title = models.CharField(max_length=250, verbose_name=_('title'))
    image = models.FileField(upload_to='biznes', verbose_name=_('biznes_image'))
    long_descriptions = RichTextUploadingField(verbose_name=_('long_descriptions'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('biznes')
        verbose_name_plural = _('biznes')


class BiznesImageModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'), null=True)

    class Meta:
        verbose_name = _('biznes_image')
        verbose_name_plural = _('biznes_image')
