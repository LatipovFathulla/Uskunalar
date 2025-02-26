from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from django import forms
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from home.models import BannerInfoModel, CategoryModel, \
    SubCategoryModel, BannerImageModel, ProductSpecificationsModel, CarouselModel, BannerBackModel, BannerCountryModel


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
class CategoryModelAdmin(SortableAdminMixin, MyTranslationAdmin):
    list_display = (format_category, 'id', 'created_at', 'my_order',)
    search_fields = ('category', 'pk')
    list_filter = ('category',)
    ordering = ['my_order']
    save_as = True

@admin.display()
def format_sub_category(obj):
    return mark_safe(obj.subcategory)


@admin.register(SubCategoryModel)
class SubCategoryModelAdmin(SortableAdminMixin, MyTranslationAdmin):
    list_display = ['category', format_sub_category, 'id', 'created_at']
    search_fields = ['subcategory', 'pk']
    list_filter = ['category', 'subcategory']
    ordering = ['my_order']


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)

            output.append(
                f'<a href="{image_url}" target="_blank">'
                f'<img src="{image_url}" alt="{file_name}" width="150" height="150" '
                f'style="object-fit: cover;"/> </a>')

        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))


class BannerImageModelAdmin(admin.TabularInline):
    model = BannerImageModel
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }


class ProductSpecificationsModelAdmin(TranslationTabularInline):
    model = ProductSpecificationsModel


class BannerForm(forms.ModelForm):
    class Meta:
        model = BannerInfoModel
        fields = '__all__'


@admin.register(BannerCountryModel)
class BannerCountryModelAdmin(admin.ModelAdmin):
    list_display = ['country', 'get_html_photo']

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}', width=200, height=100>")

    get_html_photo.short_description = "город"


@admin.register(BannerBackModel)
class BannerBackModelAdmin(admin.ModelAdmin):
    list_display = ['color', 'get_html_photo']

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}', width=200, height=100>")

    get_html_photo.short_description = "цвета"


@admin.register(BannerInfoModel)
class BannerInfoModelAdmin(MyTranslationAdmin):
    list_display = ['pk', 'title', 'city', 'created_at', 'category', 'subcategory']
    fieldsets = (
        (None, {
           "fields": (('title', 'background', 'category', 'subcategory', 'country', 'pdf', ('CIP', 'DAF', 'EXW', 'FCA'),
                       'price',  'discount', 'inbox', 'delivery', 'short_description', 'long_description', 'video'),)
        }),
        ("Price_Type", {
            "fields": (("price_title", "price_image", "price_short_description", "price_long_description"),)
        }),
    )
    search_fields = ['title', 'pk']
    list_filter = ['created_at']
    readonly_fields = ['get_price']
    form = BannerForm
    inlines = [ProductSpecificationsModelAdmin, BannerImageModelAdmin, ]
    save_on_top = True
    save_as = True
    # prepopulated_fields = {'slug': ("title",), }

    # @admin.display
    # def get_subcategories(self):
    #     return


@admin.register(CarouselModel)
class CarouselModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'descriptions', 'image', 'created_at']
    search_fields = ['title', 'descriptions', 'created_at']
    list_filter = ['title', 'created_at']
