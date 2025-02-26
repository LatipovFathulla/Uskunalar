from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WorksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'works'
    verbose_name = _('works')
