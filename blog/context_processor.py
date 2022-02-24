from home.models import CategoryModel, SubCategoryModel


def home_categories(request):
    categories = CategoryModel.objects.all()
    subcategories = SubCategoryModel.objects.order_by('-pk')

    return {
        'categories': categories,
        'subcategories': subcategories
    }
