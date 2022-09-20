import time

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from biznes.models import BiznesModel


class BiznesModelView(ListView):
    template_name = 'biznes.html'
    queryset = BiznesModel.objects.order_by('-pk')
    context_object_name = 'biznes'
    paginate_by = 7


def detail_view(request, pk):
    object = BiznesModel.objects.get(id=pk)
    object.views = object.views + 1
    object.save()

    return render(request, "single-biznes.html", context = {
        'object': object
    })
