from django.shortcuts import render
from django.views.generic import ListView

from works.models import WorkModel


class WorkModelListView(ListView):
    template_name = 'our_works.html'

    def get_queryset(self):
        qs = WorkModel.objects.order_by('-pk')

        return qs
