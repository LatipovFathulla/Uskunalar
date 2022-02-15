from django.db.models import Q, Min, Max
from django.views.generic import ListView, TemplateView

from home.models import BannerInfoModel, CategoryModel, SubCategoryModel


class BannerInfoModelView(ListView):
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self, ):
        qs = BannerInfoModel.objects.order_by('-pk')

        q = self.request.GET.get('q', '')
        category = self.request.GET.get('category')
        subcategory = self.request.GET.get('subcategory')
        sku = self.request.GET.get('sku')
        price = self.request.GET.get('price')
        sort = self.request.GET.get('sort')

        if q:
            qs = qs.filter(title__icontains=q)

        if category:
            qs = qs.filter(category_id=category)

        if subcategory:
            qs = qs.filter(category_id=subcategory)

        if sku:
            qs = qs.filter(sku_id=sku)



        if price:
            price_from, price_to = price.split(';')
            qs = qs.filter(price__gte=price_from, price__lte=price_to)

        if sort:
            if sort == 'price':
                qs = qs.order_by('price')
            elif sort == '-price':
                qs = qs.order_by('-price')

        return qs

    #
    # def get_queryset2(self, ):
    #     qs = BannerInfoModel.objects.order_by('pk')
    #
    #     q = self.request.GET.get('q', '')
    #
    #     if q:
    #         qs = qs.filter(Q(title__icontains=q) |
    #                        Q(sku__icontains=q) |
    #                        Q(city__icontains=q)
    #                        )
    #     return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.order_by('-pk')
        context['subcategories'] = SubCategoryModel.objects.order_by('-pk')

        context['min_price'], context['max_price'] = BannerInfoModel.objects.aggregate(
            Min('price'),
            Max("dollar")
        ).values()

        return context


class SingleModelView(TemplateView):
    template_name = 'single-product.html'
