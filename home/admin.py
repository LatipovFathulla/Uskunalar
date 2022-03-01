from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from home.models import BannerInfoModel, CategoryModel, SecondSubCategoryModel, \
    SubCategoryModel, BannerImageModel, ProductSpecificationsModel, CarouselModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin):
    list_display = ['category', 'created_at']
    search_fields = ['category']
    list_filter = ['category']


@admin.register(SubCategoryModel)
class SubCategoryModelAdmin(MyTranslationAdmin):
    list_display = ['category', 'subcategory', 'created_at']
    search_fields = ['category', 'subcategory']
    list_filter = ['category', 'subcategory']


@admin.register(SecondSubCategoryModel)
class SecondSubCategoryModelAdmin(MyTranslationAdmin):
    list_display = ['category', 'subcategory', 'secondsubcategory', 'created_at']
    search_fields = ['category', 'subcategory', 'secondsubcategory', ]
    list_filter = ['category', 'subcategory', 'secondsubcategory', ]


class BannerImageModelAdmin(admin.TabularInline):
    model = BannerImageModel


class ProductSpecificationsModelAdmin(admin.TabularInline):
    model = ProductSpecificationsModel


@admin.register(BannerInfoModel)
class BannerInfoModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'sku', 'dollar', 'pdf', 'city', 'created_at', 'category', 'subcategory', 'secondsubcategory', ]
    search_fields = ['title', 'sku']
    list_filter = ['created_at']
    readonly_fields = ['get_price', 'get_price_dollar']

    inlines = [ProductSpecificationsModelAdmin, BannerImageModelAdmin]


@admin.register(CarouselModel)
class CarouselModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'descriptions', 'image', 'created_at']
    search_fields = ['title', 'descriptions', 'created_at']
    list_filter = ['title', 'created_at']

