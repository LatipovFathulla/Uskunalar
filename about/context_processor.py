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
    subcategories = SubCategoryModel.objects.order_by('-pk')
    carousels = CarouselModel.objects.order_by('-pk')
    biznes = BiznesModel.objects.order_by('-pk')
    random_lines = LineModel.objects.order_by('?')[:7]
    random_line = LineModel.objects.order_by('?')[:4]
    random_prod_line = BannerInfoModel.objects.order_by('?')[:6]
    random_biznes = BiznesModel.objects.order_by('?')[:4]
    random_prod_biznes = BiznesModel.objects.order_by('?')[:6]
    random_blog = BlogModel.objects.order_by('?')[:4]
    random_prod_blog = BlogModel.objects.order_by('?')[:8]

    return {
        'products': products,
        'categories': categories,
        'lines': lines,
        'works': works,
        'blogs': blogs,
        'subcategories': subcategories,
        'carousels': carousels,
        'biznes': biznes,
        'random_lines': random_lines,
        'random_line': random_line,
        'random_prod_line': random_prod_line,
        'random_biznes': random_biznes,
        'random_prod_biznes': random_prod_biznes,
        'random_blog': random_blog,
        'random_prod_blog': random_prod_blog,
    }
