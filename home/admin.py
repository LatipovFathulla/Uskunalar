from django.contrib import admin
from django.utils.html import format_html
from django import forms
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from home.models import BannerInfoModel, CategoryModel, \
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


@admin.display()
def format_category(obj):
    return mark_safe(obj.category)


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin):
    list_display = (format_category, 'created_at',)
    search_fields = ('category',)
    list_filter = ('category',)


@admin.display()
def format_sub_category(obj):
    return mark_safe(obj.subcategory)


@admin.register(SubCategoryModel)
class SubCategoryModelAdmin(MyTranslationAdmin):
    list_display = ['category', format_sub_category, 'created_at']
    search_fields = ['category', 'subcategory']
    list_filter = ['category', 'subcategory']

class BannerImageModelAdmin(admin.TabularInline):
    model = BannerImageModel


class ProductSpecificationsModelAdmin(admin.TabularInline):
    model = ProductSpecificationsModel


class BannerForm(forms.ModelForm):
    class Meta:
        model = BannerInfoModel
        fields = '__all__'


@admin.register(BannerInfoModel)
class BannerInfoModelAdmin(MyTranslationAdmin):
    list_display = ['pk', 'title', 'dollar', 'pdf', 'city', 'created_at', 'category', 'subcategory']
    search_fields = ['title', 'pk']
    list_filter = ['created_at']
    readonly_fields = ['get_price', 'get_price_dollar']
    form = BannerForm
    inlines = [ProductSpecificationsModelAdmin, BannerImageModelAdmin]

    # @admin.display
    # def get_subcategories(self):
    #     return


@admin.register(CarouselModel)
class CarouselModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'descriptions', 'image', 'created_at']
    search_fields = ['title', 'descriptions', 'created_at']
    list_filter = ['title', 'created_at']
