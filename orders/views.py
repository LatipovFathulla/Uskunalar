from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView
from django.contrib import messages

from home.models import BannerInfoModel
from orders.forms import OrderModelForm
from orders.models import OrderModel


class OrderCreateView(CreateView):
    template_name = 'form.html'
    form_class = OrderModelForm

    def product(request, pk):
        product = get_object_or_404(BannerInfoModel, pk=pk, )
        cart_product_form = OrderModelForm()
        return render(request, 'single-product.html', {'product': product, 'cart_product_form': cart_product_form})

    def form_valid(self, form):
        form.instance.user = self.request.GET.get('name', 'phone', 'products', 'price')
        form.save()

        messages.add_message(self.request, messages.INFO, 'Успешно!')

        return super().form_valid(print(self.request.post))

    def get_success_url(self):
        return self.request.GET.get('next', '/')
