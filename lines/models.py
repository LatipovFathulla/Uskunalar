from django.db import models
from django.utils.translation import gettext_lazy as _


class LineCategoryModel(models.Model):
    category = models.CharField(max_length=100, verbose_name=_('category'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = _('line category')
        verbose_name_plural = _('line categories')


class LineModel(models.Model):
    category = models.ForeignKey(LineCategoryModel, on_delete=models.CASCADE, verbose_name=_('category'), null=True,
                                 related_name='line_categories')
    title = models.CharField(max_length=200, verbose_name=_('title'))
    image = models.FileField(upload_to='line_image', verbose_name=_('image'))
    pdf = models.FileField(upload_to='line_pdf', verbose_name=_('line_pdf'))
    description = models.TextField(verbose_name=_('description'))
    long_description = models.TextField(verbose_name=_('long_description'), null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('line')
        verbose_name_plural = _('lines')


class LineSpecificationModel(models.Model):
    line_image = models.ForeignKey(LineModel, on_delete=models.CASCADE, related_name='line_image', verbose_name=_('line_image'), null=True)
    image = models.FileField(upload_to='line_image', verbose_name=_('image'), null=True)

    class Meta:
        verbose_name = _('line specification')
        verbose_name_plural = _('line specifications')
