from django.db import models
from django.utils.translation import gettext_lazy as _

from home.models import BannerInfoModel


class OrderModel(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name=_('name'))
    phone = models.CharField(max_length=30, null=True, verbose_name=_('phone'))
    products = models.ForeignKey(BannerInfoModel, on_delete=models.PROTECT, related_name='orders', verbose_name=_('products'), null=True)
    price = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')