from django.views.generic import CreateView
from django.contrib import messages

from home.models import BannerInfoModel
from orders.forms import OrderModelForm
from orders.models import OrderModel


class OrderCreateView(CreateView):
    template_name = 'form.html'
    form_class = OrderModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = BannerInfoModel.objects.order_by('-pk')
        return context

    def form_valid(self, form):
        form.save()

        messages.add_message(self.request, messages.INFO, 'Успешно!')
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next', '/')


