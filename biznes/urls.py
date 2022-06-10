from django.urls import path
from django.views.decorators.cache import cache_page
from biznes.views import BiznesModelView, BiznesModelDetailView

app_name = 'biznes'

urlpatterns = [
    path('', cache_page(1800)(BiznesModelView.as_view()), name='biznes'),
    path('<int:pk>/', cache_page(1800)(BiznesModelDetailView.as_view()), name='detail')
]