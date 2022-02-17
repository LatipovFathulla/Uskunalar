from django.urls import path

from .views import index

app_name = 'video'

urlpatterns = [
    path('', index)
]