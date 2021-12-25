from django.db import models
from django.utils.translation import gettext_lazy as _


class BlogModel(models.Model):
    title = models.CharField(max_length=40, verbose_name=_('title'))
    image = models.ImageField(upload_to='blog', verbose_name=_('image'))
    description = models.TextField(null=True, verbose_name=_('description'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
