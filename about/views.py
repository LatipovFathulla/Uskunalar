from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, CreateView, DetailView
from django.contrib import messages
from django.core.cache import cache
from about.forms import ContactModelForm
from about.models import AboutModel
from biznes.models import BiznesModel
from blog.models import BlogModel
from home.models import BannerInfoModel, CategoryModel, SubCategoryModel
from lines.models import LineModel
from works.models import WorkModel


class AboutModelListView(ListView):
    template_name = 'about.html'
    context_object_name = 'abouts'

    def get_queryset(self):
        qs = AboutModel.objects.order_by('-pk')

        return qs


class AboutModelDetailView(DetailView):
    template_name = 'about.html'
    model = AboutModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail'] = AboutModel.objects.order_by('pk')
        return context


class ContactModelTemplateView(TemplateView):
    template_name = 'contacts.html'


class RequestCreateView(CreateView):
    template_name = 'requests.html'
    form_class = ContactModelForm

    def form_valid(self, form):
        form.save()

        messages.add_message(self.request, messages.INFO, 'Успешно!')
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next', '/')


class HomeView(TemplateView):
    template_name = 'index.html'


class NavbarView(TemplateView):
    template_name = 'header.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.order_by('-pk')

        return context


class CatalogView(TemplateView):
    template_name = 'catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.order_by('-pk')
        context['subcategories'] = SubCategoryModel.objects.order_by('-pk')

        return context
