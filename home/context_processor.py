from home.models import CategoryModel, SubCategoryModel, BannerInfoModel, ProductSpecificationsModel
from django.db.models import Min, Max
from django.utils.translation import get_language, activate


def product_categories(request, ):
    random_products = BannerInfoModel.objects.order_by('?')
    prod_spetification = ProductSpecificationsModel.objects.order_by('pk')

    current_language = get_language()
    if current_language == 'ru':
        categories = CategoryModel.objects.order_by('my_order')

    elif current_language == 'en':
        categories = CategoryModel.objects.order_by('my_order')
    else:
        categories = CategoryModel.objects.order_by('my_order')

    return {
        'categories2': categories,
        'prod_spetification': prod_spetification,
        'random_products': random_products
    }
