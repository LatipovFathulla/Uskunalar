from django.urls import path

from home.views import BannerInfoModelView, SingleModelView

app_name = 'products'

urlpatterns = [
    path('', BannerInfoModelView.as_view(), name='product'),
    path('single-product/', SingleModelView.as_view(), name='single'),
]

