from django.db.models import Q
from django.views.generic import ListView

from home.models import BannerInfoModel, CategoryModel


class BannerInfoModelView(ListView):
    template_name = 'index.html'
    context_object_name = 'banners'

    def get_queryset(self):
        qs = BannerInfoModel.objects.order_by('-pk')

        q = self.request.GET.get('q')
        category = self.request.GET.get('category')

        if q:
            qs = qs.filter(title__icontains=q)

        if category:
            qs = qs.filter(category_id=category)
        return qs

    def get_queryset(self, ):
        qs = BannerInfoModel.objects.order_by('pk')

        q = self.request.GET.get('q', '')

        if q:
            qs = qs.filter(Q(title__icontains=q) |
                           Q(sku__icontains=q) |
                           Q(city__icontains=q)
                           )
        return qs

