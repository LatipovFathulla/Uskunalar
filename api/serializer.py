from rest_framework import serializers

from home.models import BannerInfoModel, CategoryModel, SubCategoryModel, BannerBackModel, ProductSpecificationsModel


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


class BannerInfoModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    subcategory = SubCategoryModelSerializer()
    background = BannerBackgroundModelSerializer()
    specifications = ProductSpecificationsModelSerializer(many=True)

    class Meta:
        model = BannerInfoModel
        fields = '__all__'
