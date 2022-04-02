from django.shortcuts import render
from django.views.generic import ListView, DetailView

from lines.models import LineModel, LineCategoryModel, LineTextModel


class LineModelView(ListView):
    template_name = 'lines.html'
    context_object_name = 'lines'
    paginate_by = 7

    def get_queryset(self):
        qs = LineModel.objects.order_by('-pk')
        category = self.request.GET.get('category')

        if category:
            qs = qs.filter(category_id=category)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['line_categories'] = LineCategoryModel.objects.order_by('-pk')
        context['texts'] = LineTextModel.objects.order_by('pk')

        return context


class LineDetailModelView(DetailView):
    template_name = 'single-lines.html'
    model = LineModel
