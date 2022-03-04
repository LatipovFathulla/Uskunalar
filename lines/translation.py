from modeltranslation.translator import register, TranslationOptions

from lines.models import LineModel, LineCategoryModel


@register(LineCategoryModel)
class LineTranslationOptions(TranslationOptions):
    fields = ('category',)


@register(LineModel)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'category', 'description', 'long_description')

