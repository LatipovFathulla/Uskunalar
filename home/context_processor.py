from home.models import CategoryModel, SubCategoryModel
from django.core.cache import cache


def product_categories(request):
    categories = cache.get('categories')
    if not categories:
        categories = CategoryModel.objects.order_by('pk')
        cache.set('categories', categories, 10)

    subcategories = cache.get('subcategories')
    if not subcategories:
        subcategories = SubCategoryModel.objects.order_by('pk')
        cache.set('subcategories', subcategories, 10)

    return {
        'categories': categories,
        'subcategories': subcategories,
    }
