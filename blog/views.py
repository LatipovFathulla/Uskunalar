from django.shortcuts import render
from django.views.generic import ListView

from blog.models import BlogModel


class BlogModelView(ListView):
    template_name = 'blog.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        qs = BlogModel.objects.order_by('-pk')

        return qs
