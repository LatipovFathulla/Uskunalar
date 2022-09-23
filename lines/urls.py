from django.urls import path

from lines.views import LineModelView, line_view

app_name = 'line'

urlpatterns = [
    path('', LineModelView.as_view(), name="lines"),
    path('<int:pk>/', line_view, name="detail")
]