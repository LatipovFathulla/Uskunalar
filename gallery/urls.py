from django.urls import path

from gallery.views import GalleryTemplateView

app_name = 'gallery'

urlpatterns = [
    path('', GalleryTemplateView.as_view(), name='gallery')
]