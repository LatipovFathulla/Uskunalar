from modeltranslation.translator import register, TranslationOptions

from home.models import CategoryModel, SubCategoryModel, BannerInfoModel, CarouselModel


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category', 'language_code')


@register(SubCategoryModel)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('category', 'subcategory', 'language_code')


@register(BannerInfoModel)
class BannerTranslationOptions(TranslationOptions):
    fields = (
        'title', 'city', 'category', 'subcategory', 'short_description', 'long_description',
        'inbox',
        'delivery')


@register(CarouselModel)
class CarouselTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)

