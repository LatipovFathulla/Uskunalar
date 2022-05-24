from home.models import CategoryModel, SubCategoryModel, SecondSubCategoryModel
from django.core.cache import cache


def product_categories(request):
    categories = cache.get('categories')
    if not categories:
        categories = CategoryModel.objects.order_by('pk')
        cache.set('categories', categories, 60)

    subcategories = cache.get('subcategories')
    if not subcategories:
        subcategories = SubCategoryModel.objects.order_by('pk')
        cache.set('subcategories', subcategories, 60)

    secondsubcategory = cache.get('secondsubcategory')
    if not secondsubcategory:
        secondsubcategory = SecondSubCategoryModel.objects.order_by('pk')
        cache.set('secondsubcategory', secondsubcategory, 60)

    return {
        'categories': categories,
        'subcategories': subcategories,
        'secondsubcategory': secondsubcategory
    }