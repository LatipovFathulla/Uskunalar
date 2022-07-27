from api.views import BannerInfoModelAPIView
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('produdcts/', BannerInfoModelAPIView.as_view(), name='products')
]