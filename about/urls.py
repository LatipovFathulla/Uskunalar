from django.urls import path
from django.views.decorators.cache import cache_page
from about.views import AboutModelListView, \
    HomeView, CatalogView, AboutModelDetailView, RequestCreateView, ContactModelTemplateView
from orders.views import OrderCreateView

app_name = 'home'

urlpatterns = [
    path('about/', cache_page(1)(AboutModelListView.as_view()), name='about'),
    path('<int:pk>/', AboutModelDetailView.as_view(), name='detail'),
    path('contacts/', ContactModelTemplateView.as_view(), name='contacts'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('request/', RequestCreateView.as_view(), name='request'),
    path('form/', OrderCreateView.as_view(), name='form'),
    path('', cache_page(1)(HomeView.as_view()), name='home'),

]