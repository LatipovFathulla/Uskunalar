from modeltranslation.translator import register, TranslationOptions

from biznes.models import BiznesModel


@register(BiznesModel)
class BiznesTranslationOptions(TranslationOptions):
    fields = ('title', 'long_descriptions', )