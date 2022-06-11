from modeltranslation.translator import register, TranslationOptions

from videos.models import VideoModel


@register(VideoModel)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)