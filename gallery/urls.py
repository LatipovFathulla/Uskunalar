from django.urls import path

from gallery.views import GalleryTemplateView

app_name = 'galleries'

urlpatterns = [
    path('', GalleryTemplateView.as_view(), name='gallery')
]