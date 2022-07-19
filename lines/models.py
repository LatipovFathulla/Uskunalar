from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _


class LineTextModel(models.Model):
    text = models.TextField(max_length=200, verbose_name=_('text'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _('line text')
        verbose_name_plural = _('line texts')


class LineCategoryModel(models.Model):
    category = RichTextUploadingField(max_length=100, verbose_name=_('category'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return strip_tags(self.category)

    class Meta:
        verbose_name = _('line category')
        verbose_name_plural = _('line categories')


class LineModel(models.Model):
    category = models.ForeignKey(LineCategoryModel, on_delete=models.CASCADE, verbose_name=_('category'), null=True,
                                 related_name='lines')
    title = models.CharField(max_length=200, verbose_name=_('title'))
    image = models.FileField(upload_to='line_img', verbose_name=_('image'), null=True)
    banner = models.FileField(upload_to='line_image', verbose_name=_('banner'), null=True)
    pdf = models.FileField(upload_to='line_pdf', verbose_name=_('line_pdf'), null=True, blank=True)
    description = RichTextUploadingField(verbose_name=_('description'))
    price = models.CharField(max_length=100, verbose_name=_('price'), null=True)
    long_description = RichTextUploadingField(verbose_name=_('long_description'), null=True, blank=True)
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
    line_spec = models.CharField(max_length=99, verbose_name=_('line_spec'), null=True, blank=True)
    line_num = models.CharField(max_length=99, verbose_name=_('line_num'), null=True, blank=True)
    line_image = models.ForeignKey(LineModel, on_delete=models.CASCADE, related_name='line_image', verbose_name=_('line_image'), null=True, blank=True)
    image = models.FileField(upload_to='line_image', verbose_name=_('image'), null=True, blank=True)

    class Meta:
        verbose_name = _('line specification')
        verbose_name_plural = _('line specifications')
