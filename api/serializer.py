from rest_framework import serializers

from home.models import BannerInfoModel, CategoryModel, SubCategoryModel


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class SubCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryModel
        fields = '__all__'


class BannerInfoModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    subcategory = SubCategoryModelSerializer()

    class Meta:
        model = BannerInfoModel
        fields = '__all__'
