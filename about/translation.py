from modeltranslation.translator import register, TranslationOptions

from about.models import AboutModel


@register(AboutModel)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)