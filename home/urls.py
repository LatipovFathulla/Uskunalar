from django.urls import path

from home.views import BannerInfoModelView

app_name = 'banners'

urlpatterns = [
    path('', BannerInfoModelView.as_view()),
]

