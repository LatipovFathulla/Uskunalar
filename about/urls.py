from django.urls import path

from about.views import AboutModelListView
from blog.views import BlogModelView
from home.views import BannerInfoModelView

app_name = 'home'

urlpatterns = [
    path('about/', AboutModelListView.as_view(), name='about'),
    path('', BannerInfoModelView.as_view(), name='home'),
    path('blog/', BlogModelView.as_view(), name='blog')
]