from django.urls import path

from about.views import AboutModelListView
from home.views import BannerInfoModelView

app_name = 'home'

urlpatterns = [
    path('about/', AboutModelListView.as_view(), name='about'),
    path('', BannerInfoModelView.as_view(), name='home')
]