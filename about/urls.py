from django.urls import path

from about.views import AboutModelListView, \
    HomeView, CatalogView, AboutModelDetailView, RequestCreateView, ContactModelTemplateView
from orders.views import OrderCreateView

app_name = 'home'

urlpatterns = [
    path('about/', AboutModelListView.as_view(), name='about'),
    path('<int:pk>/', AboutModelDetailView.as_view(), name='detail'),
    path('contacts/', ContactModelTemplateView.as_view(), name='contacts'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('request/', RequestCreateView.as_view(), name='request'),
    path('form/', OrderCreateView.as_view(), name='form'),
    path('', HomeView.as_view(), name='home'),

]