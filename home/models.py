from datetime import datetime
from decimal import Decimal
from django.utils.html import strip_tags
from django.contrib import admin

import pytz as pytz
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from home.scrapper import _main
from django.db.models import FloatField
from django.utils.translation import gettext_lazy as _


class CategoryModel(models.Model):
    category = RichTextUploadingField(max_length=400, verbose_name=_('category'), null=True)
    image = models.FileField(upload_to='category_image', verbose_name=_('category_image'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        # return mark_safe(self.category)
        return strip_tags(self.category)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class SubCategoryModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, verbose_name=_('category'), related_name='subcategories')
    image = models.FileField(upload_to='sub_image', verbose_name=_('sub_image'), null=True, blank=True)
    subcategory = models.CharField(max_length=300, verbose_name=_('subcategory'),)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('crated_at'))

    def __str__(self):
        return self.subcategory

    class Meta:
        verbose_name = _('subcategory')
        verbose_name_plural = _('subcategories')


class BannerInfoModel(models.Model):
    title = models.CharField(max_length=99, verbose_name=_('title'), db_index=True)
    sku = models.AutoField(primary_key=True, db_index=True)
    image = models.ImageField(upload_to='banner', verbose_name=_('image'), null=True)
    pdf = models.FileField(upload_to='pdf', verbose_name=_('pdf'), null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, verbose_name=_('category'), null=True)
    subcategory = models.ForeignKey(SubCategoryModel, on_delete=models.PROTECT, verbose_name=_('subcategory'), null=True, blank=True)
    city = models.CharField(max_length=99, verbose_name=_('city'), null=True)
    price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=_('price'))
    dollar = models.IntegerField(verbose_name=_('dollar'), null=True)
    discount = models.DecimalField(default=0, max_digits=9, decimal_places=0, verbose_name=_('discount'))
    inbox = models.CharField(max_length=50,  blank=True, verbose_name=_('inbox'))
    delivery = models.CharField(max_length=50, blank=True, verbose_name=_('delivery'))
    short_description = RichTextUploadingField(verbose_name=_('short_description'), null=True)
    long_description = RichTextUploadingField(verbose_name=_('long_description'), null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def is_discount(self):
        return self.discount != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.price * self.discount / 100
        return self.price

    def get_price_dollar(self):
        if self.is_discount():
            return self.dollar - self.dollar * self.discount / 100
        return self.dollar

    def dollar_exchanges(self):
        return self.price * Decimal(_main())

    def is_new(self):
        diff = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return diff.days <= 3

    @staticmethod
    def get_from_wishlist(request):
        wishlist = request.session.get('wishlist', [])
        return BannerInfoModel.objects.filter(pk__in=wishlist)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('products')
        verbose_name_plural = _('products')
        ordering = ['title']


class BannerImageModel(models.Model):
    product = models.ForeignKey(BannerInfoModel, on_delete=models.CASCADE, related_name='images',
                                verbose_name=_('product'), null=True, blank=True)
    image = models.ImageField(upload_to='products', verbose_name=_('image'), null=True, blank=True)

    class Meta:
        verbose_name = _('product image')
        verbose_name_plural = _('product images')


class ProductSpecificationsModel(models.Model):
    product = models.ForeignKey(BannerInfoModel, on_delete=models.CASCADE, related_name='specifications', null=True,blank=True, verbose_name=_('products'))
    product_customer = models.CharField(max_length=99, verbose_name=_('product_customer'), null=True, blank=True)
    product_number = models.CharField(max_length=99, verbose_name=_('product_numbers'), null=True, blank=True)
    product_image = models.FileField(upload_to='pdf_image', verbose_name=_('product_image'), null=True, blank=True)

    class Meta:
        verbose_name = _('product specification')
        verbose_name_plural = _('product specifications')


class CarouselModel(models.Model):
    title = models.CharField(max_length=60, verbose_name=_('title'))
    descriptions = models.TextField(verbose_name=_('descriptions'))
    image = models.FileField(upload_to='Banner_home1', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('carousel')
        verbose_name_plural = _('carousels')


# translate
# Header and footer
# 1.Create models to blog:(for)-see more
#     1.image,banner-image,title,price,send to social networks,description,specifications,buy now(form),save PDF file.
# 2.Create categorymodels:
#     1.Category name,category_title.
# 3.Crete Productmodels(for):
#     1.image,banner-image,name,id,price($) and price(SOM),see more CAROUSEL
# 4.Create VideoModels:
#     1.Iframe youtube or video models,created_at,title
# 5.ProjectsModel(for):see-more
#     1.Image,title,see more
#     2.title,banner-image, description and buy or PDF
# 6.Articles(for):see-more
#     1.Image,banner-image,title,description and buy or PDF
# 7.Form
#     1.Title,name,phone,send


# PRODUCTS
# 1.create category filter
# 2.create all,have a storage and filter all a-z,z-a,top products,new products,price 1-100
# 3.create products(for):
#     1.image,name,price($) and price(SOM), see more
# 4.Product info
#     1.image1-2,name product,price($) and price(SOM),text,ID,buy and PDF, link social links,scpetifications,recommentation products CAROUSEL
# 5.ProjectsModel(for):see-more HEADER
#     1.Image,title,see more
#     2.title,banner-image, description and buy or PDF


# back to top ))

# jivo
