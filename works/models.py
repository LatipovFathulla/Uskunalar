from django.db import models
from django.utils.translation import gettext_lazy as _


class WorkModel(models.Model):
    title = models.CharField(max_length=99, verbose_name=_('title'))
    image = models.ImageField(upload_to='works', verbose_name=_('works'))
    descriptions = models.TextField(verbose_name=_('descriptions'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'work'
        verbose_name_plural = 'works'