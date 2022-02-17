from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from about.models import AboutModel
from home.models import BannerInfoModel


class AboutModelListView(ListView):
    template_name = 'about.html'
    context_object_name = 'abouts'

    def get_queryset(self):
        qs = AboutModel.objects.order_by('-pk')

        return qs


class ContactModelTemplateView(TemplateView):
    template_name = 'contacts.html'


class HomeView(TemplateView):
    template_name = 'index.html'


class CatalogView(TemplateView):
    template_name = 'catalog.html'