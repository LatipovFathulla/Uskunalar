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


class LineSpecificationModel(models.Model):
    title = models.ForeignKey(LineModel, on_delete=models.CASCADE, related_name='line', verbose_name=_('title'))
    line_specification = models.CharField(max_length=90, verbose_name=_('line_specification'))
    line_number = models.CharField(max_length=90, verbose_name=_('line_number'))

    class Meta:
        verbose_name = _('line specification')
        verbose_name_plural = _('line specifications')
