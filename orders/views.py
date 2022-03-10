from django.views.generic import CreateView

from home.models import BannerInfoModel
from orders.forms import OrderModelForm


class OrderCreateView(CreateView):
    template_name = 'form.html'
    form_class = OrderModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = BannerInfoModel.objects.order_by('-pk')
        return context
