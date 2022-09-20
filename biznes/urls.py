from django.urls import path
from biznes.views import BiznesModelView, detail_view

app_name = 'biznes'

urlpatterns = [
    path('', BiznesModelView.as_view(), name='biznes'),
    path('<int:pk>/', detail_view, name='detail')
]