from django.urls import path

from about.views import AboutModelListView, ContactModelTemplateView, VideoModelListView, WishlistModelListView, \
    HomeView, CatalogView

app_name = 'home'

urlpatterns = [
    path('about/', AboutModelListView.as_view(), name='about'),
    path('contacts/', ContactModelTemplateView.as_view(), name='contacts'),
    path('videos/', VideoModelListView.as_view(), name='videos'),
    path('wishlist/', WishlistModelListView.as_view(), name='wishlist'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('', HomeView.as_view(), name='home'),

]