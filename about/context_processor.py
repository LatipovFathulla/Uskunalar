from biznes.models import BiznesModel
from blog.models import BlogModel
from home.models import BannerInfoModel, CategoryModel, SubCategoryModel, SecondSubCategoryModel
from lines.models import LineModel
from works.models import WorkModel


def index_categories(request):
    products = BannerInfoModel.objects.order_by('-pk')[:8]
    categories = CategoryModel.objects.order_by('pk')
    categories2 = CategoryModel.objects.order_by('pk')
    lines = LineModel.objects.order_by('-pk')[:8]
    works = WorkModel.objects.order_by('-pk')[:4]
    blogs = BlogModel.objects.order_by('-pk')
    subcategories = SubCategoryModel.objects.order_by('-pk')
    biznes = BiznesModel.objects.order_by('-pk')

    return {
        'products': products,
        'categories': categories,
        'categories2': categories2,
        'lines': lines,
        'works': works,
        'blogs': blogs,
        'subcategories': subcategories,
        'biznes': biznes
    }
