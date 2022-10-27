from django.urls import path
from django.views.decorators.cache import cache_page
from about.views import AboutModelListView, \
    HomeView, AboutModelDetailView, RequestCreateView, ContactModelTemplateView

app_name = 'home'

urlpatterns = [
    path('about/', cache_page(1800)(AboutModelListView.as_view()), name='about'),
    path('<int:pk>/', AboutModelDetailView.as_view(), name='detail'),
    path('contacts/', ContactModelTemplateView.as_view(), name='contacts'),
    path('request/', RequestCreateView.as_view(), name='request'),
]