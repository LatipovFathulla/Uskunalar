from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BiznesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'biznes'
    verbose_name = _('biznes')
