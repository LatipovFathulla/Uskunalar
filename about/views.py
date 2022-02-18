from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, TemplateView, CreateView

from about.forms import RequestModelForm
from about.models import AboutModel
from blog.models import BlogModel
from home.models import BannerInfoModel, CategoryModel
from lines.models import LineModel
from works.models import WorkModel


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = BannerInfoModel.objects.order_by('-pk')[:8]
        context['categories'] = CategoryModel.objects.order_by('-pk')[:9]
        context['categories2'] = CategoryModel.objects.order_by('-pk')
        context['lines'] = LineModel.objects.order_by('-pk')[:8]
        context['works'] = WorkModel.objects.order_by('-pk')[:4]
        context['blogs'] = BlogModel.objects.order_by('-pk')

        return context


class CatalogView(TemplateView):
    template_name = 'catalog.html'


class RequestCreateView(CreateView):
    form_class = RequestModelForm
    template_name = 'request.html'

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home:about')