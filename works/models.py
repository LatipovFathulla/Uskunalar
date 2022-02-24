from django.db import models
from django.utils.translation import gettext_lazy as _


class WorkModel(models.Model):
    title = models.CharField(max_length=99, verbose_name=_('title'))
    image = models.ImageField(upload_to='works', verbose_name=_('works'))
    short_descriptions = models.TextField(verbose_name=_('short_descriptions'), max_length=520, null=True)
    descriptions = models.TextField(verbose_name=_('descriptions'))
    created_at = models.DateTimeField(auto_now_add=True)

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('work')
        verbose_name_plural = _('works')


class WorkImageModel(models.Model):
    work_image = models.ForeignKey(WorkModel, on_delete=models.CASCADE, related_name='work_image', verbose_name=_('work_image'))
    image = models.FileField(upload_to='work_single', verbose_name=_('work_image'))

    class Meta:
        verbose_name = _('work_image')
        verbose_name_plural = _('work_image')


class WorkSpecificationsModel(models.Model):
    work = models.ForeignKey(WorkModel, on_delete=models.CASCADE, related_name='work', verbose_name=_('work'))
    work_customer = models.CharField(max_length=99, verbose_name=_('work_customer'))
    work_number = models.CharField(max_length=99, verbose_name=_('work_numbers'))
    work_image = models.FileField(upload_to='pdf_image', verbose_name=_('work_image'), null=True, blank=True)

    class Meta:
        verbose_name = _('work specification')
        verbose_name_plural = _('work specifications')


