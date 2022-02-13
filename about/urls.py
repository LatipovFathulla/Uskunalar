from django.urls import path

from about.views import AboutModelListView, ContactModelTemplateView, VideoModelListView, WishlistModelListView
from blog.views import BlogModelView
from home.views import BannerInfoModelView

app_name = 'home'

urlpatterns = [
    path('about/', AboutModelListView.as_view(), name='about'),
    path('contacts/', ContactModelTemplateView.as_view(), name='contacts'),
    path('videos/', VideoModelListView.as_view(), name='videos'),
    path('wishlist/', WishlistModelListView.as_view(), name='wishlist'),
    path('', BannerInfoModelView.as_view(), name='home'),

]