from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import BlogModel


class BlogModelView(ListView):
    template_name = 'blog.html'
    context_object_name = 'blogs'
    paginate_by = 1

    def get_queryset(self):
        qs = BlogModel.objects.order_by('-pk')

        return qs


class SingleBlogView(DetailView):
    template_name = 'single-blog.html'
    model = BlogModel
