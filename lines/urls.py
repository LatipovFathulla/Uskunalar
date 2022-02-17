from django.urls import path

from lines.views import LineModelView

app_name = 'line'

urlpatterns = [
    path('', LineModelView.as_view(), name="lines")
]