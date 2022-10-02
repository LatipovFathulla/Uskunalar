from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import BlogModel


class BlogModelView(ListView):
    template_name = 'blog.html'
    context_object_name = 'blogs'
    paginate_by = 7

    def get_queryset(self):
        qs = BlogModel.objects.order_by('-pk')

        return qs


def blog_view(request, pk):
    object = BlogModel.objects.get(id=pk)
    object.views = object.views + 1
    object.save()

    return render(request, "single-blog.html", context = {
        'object': object
    })
