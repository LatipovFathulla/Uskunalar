from modeltranslation.translator import register, TranslationOptions

from gallery.models import GalleryModel


@register(GalleryModel)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('title', 'short_descriptions', 'long_descriptions')