from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from home.models import BannerInfoModel, SingleBannerModel, CategoryModel, ErrorModel, SecondSubCategoryModel, \
    SubCategoryModel


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
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category', 'created_at']
    search_fields = ['category']
    list_filter = ['category']


@admin.register(SubCategoryModel)
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category', 'subcategory', 'created_at']
    search_fields = ['category', 'subcategory']
    list_filter = ['category', 'subcategory']


@admin.register(SecondSubCategoryModel)
class SecondSubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category', 'subcategory', 'secondsubcategory', 'created_at']
    search_fields = ['category', 'subcategory', 'secondsubcategory',]
    list_filter = ['category', 'subcategory', 'secondsubcategory',]


@admin.register(BannerInfoModel)
class BannerInfoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'sku', 'price', 'price_dollar', 'get_price', 'get_price_dollar', 'created_at',
                    'discount', 'inbox', 'delivery', 'category', 'subcategory', 'secondsubcategory',]
    search_fields = ['title', 'sku']
    list_filter = ['created_at']

    readonly_fields = ['get_price', 'get_price_dollar']


@admin.register(SingleBannerModel)
class SingleBannerModelAdmin(admin.ModelAdmin):
    list_display = ['banner_title', 'banner_sku', 'banner_price', 'banner_price_dollar']
    search_fields = ['banner_title', 'banner_sku']
    list_filter = ['created_at']


@admin.register(ErrorModel)
class ErrorModelAdmin(admin.ModelAdmin):
    list_display = ['error', ]
    search_fields = ['error']
    list_filter = ['error', ]
