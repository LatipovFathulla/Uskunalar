from django.db.models import Q
from django.views.generic import ListView, TemplateView

from home.models import BannerInfoModel, CategoryModel, SubCategoryModel


class BannerInfoModelView(ListView):
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        qs = BannerInfoModel.objects.order_by('-pk')

        q = self.request.GET.get('q')
        category = self.request.GET.get('category')
        sku = self.request.GET.get('sku')

        if q:
            qs = qs.filter(title__icontains=q)

        if category:
            qs = qs.filter(category_id=category)

        if sku:
            qs = qs.filter(sku__icontains=sku)

        return qs

    def get_queryset2(self, ):
        qs = BannerInfoModel.objects.order_by('pk')

        q = self.request.GET.get('q', '')

        if q:
            qs = qs.filter(Q(title__icontains=q) |
                           Q(sku__icontains=q) |
                           Q(city__icontains=q)
                           )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.order_by('-pk')
        context['subcategories'] = SubCategoryModel.objects.order_by('-pk')

        return context


class SingleModelView(TemplateView):
    template_name = 'single-product.html'
