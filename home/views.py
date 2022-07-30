from datetime import datetime

import pytz
from django.db.models import Q, Min, Max
from django.http import JsonResponse, HttpResponse
import json
from django.views.generic import ListView, TemplateView, DetailView
from rest_framework.response import Response

from home.models import BannerInfoModel, CategoryModel, SubCategoryModel
from home.utils import get_wishlist_data


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

class BannerInfoModelView(ListView):
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self, ):
        q = self.request.GET.get('q', '')
        category = self.request.GET.get('category')
        subcategory = self.request.GET.get('subcategory')
        price = self.request.GET.get('price')
        sort = self.request.GET.get('sort')
        som = self.request.GET.get('price')
        created_at = self.request.GET.get('created_at')
        inbox = self.request.GET.get('inbox')
        delivery = self.request.GET.get('delivery')

        filters = {}
        order_by = ['-pk']
        if q:
            filters['title__icontains'] = q

        if category:
            filters['category_id'] = category

        if subcategory:
            filters['subcategory_id'] = subcategory

        if price:
            price_from, price_to = price.split(';')
            filters['price__gte'] = price_from
            filters['price__lte'] = price_to

        if inbox:
            if inbox == 'inbox':
                order_by.append('inbox')
        if delivery:
            if delivery == 'delivery':
                order_by.append('delivery')

        if created_at == 'created_at':
            order_by.append('created_at')
            # diff = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
            # return diff.days <= 3
        qs = BannerInfoModel.objects.select_related('category', 'category_uz', 'category_ru', 'category_en').filter(
            **filters).order_by(*order_by)

        if sort:
            if sort == 'price':
                qs = sorted(qs, key=lambda i: i.get_price())
            elif sort == '-price':
                qs = sorted(qs, key=lambda i: i.get_price(), reverse=True)

        if som:
            if som == 'som':
                qs = sorted(qs, key=lambda i: i.get_price())
            elif som == '-som':
                qs = sorted(qs, key=lambda i: i.get_price(), reverse=True)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['min_price'], context['max_price'] = BannerInfoModel.objects.aggregate(
            Min('price'),
            Max('price')
        ).values()

        return context


def get_subcategory(request):
    pk = request.GET.get('pk', '')
    result = list(SubCategoryModel.objects.filter(category_id=pk).values('pk', 'subcategory'))
    return HttpResponse(json.dumps(result), content_type="application/json")


class SingleModelDetailView(DetailView):
    template_name = 'single-product.html'
    model = BannerInfoModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = BannerInfoModel.objects.order_by('-pk')
        return context


class WishlistModelListView(ListView):
    template_name = 'wishlist.html'
    paginate_by = 7

    def get_queryset(self):
        return BannerInfoModel.get_from_wishlist(self.request)


def add_to_wishlist(request, pk):
    try:
        product = BannerInfoModel.objects.get(pk=pk)
    except BannerInfoModel.DoesNotExist:
        return Response(data={'status': False})
        # if not wishlist:
        #     wishlist = []
    wishlist = request.session.get('wishlist', [])
    if product.pk in wishlist:
        wishlist.remove(product.pk)
        data = {'status': True, 'added': False}
    else:
        wishlist.append(product.pk)
        data = {'status': True, 'added': True}
    request.session['wishlist'] = wishlist

    data['wishlist_len'] = get_wishlist_data(wishlist)
    return JsonResponse(data)


class CategoryTest(TemplateView):
    template_name = 'test.html'
