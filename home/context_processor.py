from home.models import CategoryModel, SubCategoryModel


def product_categories(request):
    categories = CategoryModel.objects.order_by('pk')
    subcategories = SubCategoryModel.objects.order_by('pk')

    return {
        'categories': categories,
        'subcategories': subcategories,
    }
