from django.shortcuts import render
from django.views.generic import ListView

from about.models import AboutModel


class AboutModelListView(ListView):
    template_name = 'about2.html'
    context_object_name = 'abouts'

    def get_queryset(self):
        qs = AboutModel.objects.order_by('-pk')

        return qs
