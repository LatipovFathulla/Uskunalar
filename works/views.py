from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from works.models import WorkModel


class WorkModelListView(ListView):
    template_name = 'our_works.html'
    paginate_by = 9

    def get_queryset(self):
        qs = WorkModel.objects.order_by('-pk')

        return qs


class SingleWorkTemplateView(DetailView):
    template_name = 'single-work.html'
    model = WorkModel
