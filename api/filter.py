import django_filters

from home.models import BannerInfoModel, CategoryModel, SubCategoryModel


class ProductFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(field_name='category', queryset=CategoryModel.objects.all())
    subcategory = django_filters.ModelChoiceFilter(field_name='subcategory', queryset=SubCategoryModel.objects.all())
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = BannerInfoModel
        fields = ['category', 'subcategory', 'price']
