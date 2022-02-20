from django.urls import path

from works.views import WorkModelListView, SingleWorkTemplateView

app_name = 'work'

urlpatterns = [
    path('', WorkModelListView.as_view(), name='works'),
    path('<int:pk>/', SingleWorkTemplateView.as_view(), name='single-work')
]