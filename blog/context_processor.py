from home.models import CategoryModel, SubCategoryModel


def home_categories(request):
    categories = CategoryModel.objects.all()
    subcategories = SubCategoryModel.objects.select_related("category_ru", "category_uz", "category", "category_en", "category_ru_id", "asdasd").values_list('category__pk', flat=True).order_by('-pk')

    return {
        'categories': categories,
        'subcategories': subcategories
    }
