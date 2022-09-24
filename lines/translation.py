from modeltranslation.translator import register, TranslationOptions

from lines.models import LineModel, LineCategoryModel, LineTextModel


@register(LineTextModel)
class LineTextTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(LineCategoryModel)
class LineTranslationOptions(TranslationOptions):
    fields = ('category',)


@register(LineModel)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'long_description')

