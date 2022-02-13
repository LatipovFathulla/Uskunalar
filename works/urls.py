from django.urls import path

from works.views import WorkModelListView

app_name = 'work'

urlpatterns = [
    path('', WorkModelListView.as_view(), name='works')
]