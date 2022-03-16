from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _


class BlogModel(models.Model):
    title = models.CharField(max_length=40, verbose_name=_('title'))
    image = models.ImageField(upload_to='blog', verbose_name=_('image'))
    description = RichTextUploadingField(null=True, verbose_name=_('description'))
    smart_description = RichTextUploadingField(null=True, blank=True, verbose_name=_('smart_description'))
    smart_text = RichTextUploadingField(null=True, blank=True, verbose_name=_('smart_text'))
    created_at = models.DateTimeField(auto_now_add=True)

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')
