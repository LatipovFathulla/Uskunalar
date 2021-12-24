from django.core.handlers import exception
from django.db.models import Q
from django.http import Http404, request
from django.shortcuts import render
from django.template import RequestContext
from django.views import defaults
from django.views.generic import ListView

from home.models import BannerInfoModel, SingleBannerModel


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
                           Q(sku__icontains=q)
                           )
        return qs


class SingleBannerModelView(ListView):
    template_name = 'single-product.html'
    context_object_name = 'single'

    def get_queryset(self):
        qs = SingleBannerModel.objects.all()

        return qs

