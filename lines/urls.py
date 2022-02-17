from django.urls import path

from lines.views import LineModelView, LineDetailModelView

app_name = 'line'

urlpatterns = [
    path('', LineModelView.as_view(), name="lines"),
    path('<int:pk>/', LineDetailModelView.as_view(), name="detail")
]