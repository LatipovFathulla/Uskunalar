from django.shortcuts import get_object_or_404, render, redirect
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

    def get_success_url(self):
        return self.request.GET.get('next', '/')

    def form_valid(self, form):
        pk = self.request.POST.get('products')
        product = BannerInfoModel.objects.get(pk=pk)
        print(pk, product)
        form.instance.user = self.request.POST.get('name')
        form.instance.phone = self.request.POST.get('phone')
        form.instance.category = self.request.POST.get('category')
        form.instance.products = product
        form.instance.price = self.request.POST.get('price')
        messages.add_message(self.request, messages.INFO, 'Успешно!')
        form.save()

        return redirect(self.get_success_url())


