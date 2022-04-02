from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LinesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lines'
    verbose_name = _('lines_categories')
