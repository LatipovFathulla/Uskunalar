from django.db import models
from django.utils.translation import gettext_lazy as _


class ClientModel(models.Model):
    image = models.FileField(upload_to='client_images', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    class Meta:
        verbose_name = _('partner')
        verbose_name_plural = _('partners')
