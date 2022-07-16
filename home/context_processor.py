from home.models import CategoryModel, SubCategoryModel, BannerInfoModel, ProductSpecificationsModel
from django.db.models import Min, Max
from django.utils.translation import get_language, activate


def product_categories(request, ):
    prod_spetification = ProductSpecificationsModel.objects.order_by('pk')

    current_language = get_language()
    if current_language == 'ru':
        categories = CategoryModel.objects.order_by('-pk')
        subcategories = SubCategoryModel.objects.order_by('pk')

    elif current_language == 'en':
        categories = CategoryModel.objects.order_by('-pk')
        subcategories = SubCategoryModel.objects.order_by('pk')
    else:
        categories = CategoryModel.objects.order_by('-pk')
        subcategories = SubCategoryModel.objects.order_by('pk')

    return {
        'categories2': categories,
        'subcategories2': subcategories,
        'prod_spetification': prod_spetification
    }
