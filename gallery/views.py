from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from gallery.models import GalleryModel


class GalleryTemplateView(ListView):
    model = GalleryModel
    template_name = 'gallery.html'
    queryset = GalleryModel.objects.order_by('-pk')
    paginate_by = 6
    context_object_name = 'galleries'
