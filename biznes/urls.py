from django.urls import path
from biznes.views import BiznesModelView, BiznesModelDetailView

app_name = 'biznes'

urlpatterns = [
    path('', BiznesModelView.as_view(), name='biznes'),
    path('<int:pk>/', BiznesModelDetailView.as_view(), name='detail')
]