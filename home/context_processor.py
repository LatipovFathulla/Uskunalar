from home.models import CategoryModel, SubCategoryModel
from django.core.cache import cache


def product_categories(request):
    categories = CategoryModel.objects.order_by('pk')
    subcategories = SubCategoryModel.objects.order_by('pk')

    return {
        'categories': categories,
        'subcategories': subcategories,
    }
