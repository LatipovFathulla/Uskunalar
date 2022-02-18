from django.urls import path

from about.views import AboutModelListView, ContactModelCreateView, \
    HomeView, CatalogView

app_name = 'home'

urlpatterns = [
    path('about/', AboutModelListView.as_view(), name='about'),
    path('contacts/', ContactModelCreateView.as_view(), name='contacts'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('', HomeView.as_view(), name='home'),

]