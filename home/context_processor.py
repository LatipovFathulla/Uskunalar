from home.models import CategoryModel, SubCategoryModel, BannerInfoModel
from django.db.models import Min, Max


def product_categories(request, ):
    categories = CategoryModel.objects.order_by('pk')
    subcategories = SubCategoryModel.objects.order_by('pk')
    # min_price = BannerInfoModel.objects.aggregate(Min('dollar')
    # max_price = BannerInfoModel.objects.aggregate(Max('dollar')

    return {
        'categories': categories,
        'subcategories': subcategories,
        # 'min_price': min_price,
        # 'max_price': max_price,
    }
