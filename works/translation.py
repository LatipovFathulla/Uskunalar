from modeltranslation.translator import register, TranslationOptions

from works.models import WorkModel


@register(WorkModel)
class WorkTranslationOptions(TranslationOptions):
    fields = ('title', 'short_descriptions', 'descriptions')