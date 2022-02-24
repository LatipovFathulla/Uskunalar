from modeltranslation.translator import register, TranslationOptions

from home.models import CategoryModel, SubCategoryModel, SecondSubCategoryModel, BannerInfoModel


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category',)


@register(SubCategoryModel)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('category', 'subcategory')


@register(SecondSubCategoryModel)
class SecondCategoryTranslationOptions(TranslationOptions):
    fields = ('category', 'subcategory', 'secondsubcategory')


@register(BannerInfoModel)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'city', 'category', 'subcategory', 'secondsubcategory')


