from api.views import BannerInfoModelAPIView
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('products/', BannerInfoModelAPIView.as_view(), name='products')
]