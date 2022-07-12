from home.models import CategoryModel, SubCategoryModel, BannerInfoModel
from django.db.models import Min, Max


def product_categories(request, ):
    categories = CategoryModel.objects.select_related("category_ru_id").values_list('id', flat=True).order_by('pk').distinct('id')
    subcategories = SubCategoryModel.objects.select_related("category_ru", "category_uz", "category", "category_en", "category_ru_id").values_list('category__pk', flat=True).order_by('pk').distinct('category__pk')
    # min_price = BannerInfoModel.objects.aggregate(Min('dollar')
    # max_price = BannerInfoModel.objects.aggregate(Max('dollar')

    return {
        'categories': categories,
        'subcategories': subcategories,
        # 'min_price': min_price,
        # 'max_price': max_price,
    }
