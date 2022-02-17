from django.db import models
from django.utils.translation import gettext_lazy as _


class LineModel(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    image = models.FileField(upload_to='line_image', verbose_name=_('image'))
    pdf = models.FileField(upload_to='line_pdf', verbose_name=_('line_pdf'))
    description = models.TextField(verbose_name=_('description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('line')
        verbose_name_plural = _('lines')
