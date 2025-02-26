from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _


class BiznesModel(models.Model):
    title = models.CharField(max_length=250, verbose_name=_('title'), null=True, blank=True)
    image = models.FileField(upload_to='biznes', verbose_name=_('biznes_image'))
    long_descriptions = RichTextUploadingField(verbose_name=_('long_descriptions'))
    views = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    def __str__(self):
        return strip_tags(self.title)

    def get_absolute_url(self):
        return reverse('biznes:detail', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = _('biznes')
        verbose_name_plural = _('biznes')
        ordering = ['-pk']


class BiznesImageModel(models.Model):
    biznes_image = models.ForeignKey(BiznesModel, on_delete=models.CASCADE, related_name='biznes_image', verbose_name=_('biznes_image'), null=True, blank=True)
    biznes_spec = models.CharField(max_length=200, verbose_name=_('biznes_spec'), null=True, blank=True)
    biznes_num = models.CharField(max_length=200, verbose_name=_('biznes_num'), null=True, blank=True)
    image = models.FileField(upload_to='biznes_single', verbose_name=_('biznes_image'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'), null=True)

    class Meta:
        verbose_name = _('biznes_image')
        verbose_name_plural = _('biznes_image')
