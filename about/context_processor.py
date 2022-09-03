from biznes.models import BiznesModel
from blog.models import BlogModel
from home.models import BannerInfoModel, CategoryModel, SubCategoryModel, CarouselModel
from lines.models import LineModel
from works.models import WorkModel


def index_categories(request):
    products = BannerInfoModel.objects.order_by('?')[:16]
    categories = CategoryModel.objects.order_by('my_order')
    lines = LineModel.objects.order_by('?')[:8]
    works = WorkModel.objects.order_by('-pk')[:4]
    blogs = BlogModel.objects.order_by('-pk')
    subcategories = SubCategoryModel.objects.select_related("category_ru", "category_uz", "category", "category_en",).\
        values_list('category__pk', flat=True).order_by('-pk')
    carousels = CarouselModel.objects.order_by('-pk')
    biznes = BiznesModel.objects.order_by('-pk')

    return {
        'products': products,
        'categories': categories,
        'lines': lines,
        'works': works,
        'blogs': blogs,
        'subcategories': subcategories,
        'carousels': carousels,
        'biznes': biznes
    }
