from home.models import CategoryModel, SubCategoryModel, BannerInfoModel, ProductSpecificationsModel
from django.db.models import Min, Max
from django.utils.translation import get_language, activate


def product_categories(request, ):
    prod_spetification = ProductSpecificationsModel.objects.order_by('pk')

    current_language = get_language()
    # print(current_language)
    if current_language == 'ru':
        categories = CategoryModel.objects.filter(language_code_ru=current_language.upper()).order_by('-pk')
        # print(categories[0].category_uz)
        subcategories = SubCategoryModel.objects.filter(language_code__contains=current_language.upper()).order_by('pk')

    elif current_language == 'en':
        categories = CategoryModel.objects.filter(language_code=current_language.upper()).order_by('-pk')
        subcategories = SubCategoryModel.objects.filter(language_code=current_language.upper()).order_by('pk')
    else:
        categories = CategoryModel.objects.filter(language_code=current_language.upper()).order_by('-pk')
        subcategories = SubCategoryModel.objects.filter(language_code=current_language.upper()).order_by('pk')
        # print(categories)
        # subcategories = SubCategoryModel.objects.filter()
    # activate(current_language)
    # min_price = BannerInfoModel.objects.aggregate(Min('dollar')
    # max_price = BannerInfoModel.objects.aggregate(Max('dollar')

    return {
        'categories2': categories,
        'subcategories2': subcategories,
        'prod_spetification': prod_spetification
        # 'min_price': min_price,
        # 'max_price': max_price,
    }
