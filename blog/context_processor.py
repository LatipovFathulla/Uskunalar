from home.models import CategoryModel, SubCategoryModel


def home_categories(request):
    categories = CategoryModel.objects.all()

    return {
        'categories': categories,
    }
