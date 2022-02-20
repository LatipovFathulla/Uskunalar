from django.shortcuts import render
from django.views.generic import ListView, DetailView

from biznes.models import BiznesModel


class BiznesModelView(ListView):
    template_name = 'biznes.html'
    queryset = BiznesModel.objects.order_by('-pk')
    context_object_name = 'biznes'


class BiznesModelDetailView(DetailView):
    model = BiznesModel
    template_name = 'single-biznes.html'

