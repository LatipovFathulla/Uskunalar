from django.shortcuts import render
from django.views.generic import ListView, DetailView

from lines.models import LineModel


class LineModelView(ListView):
    template_name = 'lines.html'
    queryset = LineModel.objects.order_by('-pk')
    context_object_name = 'lines'
    paginate_by = 7


class LineDetailModelView(DetailView):
    template_name = 'single-lines.html'
    model = LineModel
