from modeltranslation.translator import register, TranslationOptions

from home.models import CategoryModel, SubCategoryModel, BannerInfoModel, CarouselModel, ProductSpecificationsModel


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category',)


@register(ProductSpecificationsModel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_customer', 'product_number')


@register(SubCategoryModel)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('category', 'subcategory',)


@register(BannerInfoModel)
class BannerTranslationOptions(TranslationOptions):
    fields = (
        'title', 'city', 'category', 'subcategory', 'short_description', 'long_description',
        'inbox',
        'delivery')


@register(CarouselModel)
class CarouselTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)
