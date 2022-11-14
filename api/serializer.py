from rest_framework import serializers

from about.models import AboutModel
from biznes.models import BiznesModel
from blog.models import BlogModel
from clients.models import ClientModel
from gallery.models import GalleryModel
from home.models import BannerInfoModel, CategoryModel, SubCategoryModel, BannerBackModel, ProductSpecificationsModel, \
    BannerImageModel, CarouselModel
from lines.models import LineModel, LineCategoryModel
from videos.models import VideoModel
from works.models import WorkModel


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class SubCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryModel
        fields = '__all__'


class BannerBackgroundModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerBackModel
        fields = ['color', 'image']


class ProductSpecificationsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecificationsModel
        exclude = ['product']


class BannerImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImageModel
        exclude = ['product']


class BannerInfoModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    subcategory = SubCategoryModelSerializer()
    background = BannerBackgroundModelSerializer()
    specifications = ProductSpecificationsModelSerializer(many=True)
    images = BannerImageModelSerializer(many=True)

    class Meta:
        model = BannerInfoModel
        fields = '__all__'


# lines
class LineCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineCategoryModel
        fields = '__all__'


class LinesModelSerializer(serializers.ModelSerializer):
    category = LineCategoryModelSerializer()

    class Meta:
        model = LineModel
        fields = '__all__'


# biznes
class BiznesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiznesModel
        fields = '__all__'


# videos
class VideoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoModel
        fields = '__all__'


# blogs
class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'


# about
class AboutModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutModel
        fields = '__all__'


# gallery
class GalleryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryModel
        fields = '__all__'


# works
class WorkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkModel
        fields = '__all__'


# Carousel
class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselModel
        fields = '__all__'


# Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


# Subcategory
class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = SubCategoryModel
        exclude = ['category_uz', 'category_ru', 'category_en']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'