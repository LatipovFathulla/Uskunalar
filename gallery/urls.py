from django.urls import path

from gallery.views import GalleryTemplateView, SingleGalleryDetailView

app_name = 'galleries'

urlpatterns = [
    path('<int:pk>/', SingleGalleryDetailView.as_view(), name='single'),
    path('', GalleryTemplateView.as_view(), name='gallery')
]