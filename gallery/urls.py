from django.urls import path
from django.views.decorators.cache import cache_page
from gallery.views import GalleryTemplateView, SingleGalleryDetailView

app_name = 'galleries'

urlpatterns = [
    path('<int:pk>/', cache_page(1800)(SingleGalleryDetailView.as_view()), name='single'),
    path('', cache_page(1800)(GalleryTemplateView.as_view()), name='gallery')
]