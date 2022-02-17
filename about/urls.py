from django.urls import path

from about.views import AboutModelListView, ContactModelTemplateView, \
    HomeView, CatalogView, RequestCreateView

app_name = 'home'

urlpatterns = [
    path('about/', AboutModelListView.as_view(), name='about'),
    path('contacts/', ContactModelTemplateView.as_view(), name='contacts'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('request/', RequestCreateView.as_view(), name='request'),
    path('', HomeView.as_view(), name='home'),

]