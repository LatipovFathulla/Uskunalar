from django.shortcuts import render
from django.views.generic import ListView

from lines.models import LineModel


class LineModelView(ListView):
    template_name = 'lines.html'
    queryset = LineModel.objects.order_by('-pk')
