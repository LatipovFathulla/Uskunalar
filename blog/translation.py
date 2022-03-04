from modeltranslation.translator import register, TranslationOptions

from blog.models import BlogModel


@register(BlogModel)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description',  'smart_description', 'smart_text')