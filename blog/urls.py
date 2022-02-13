from django.urls import path

from blog.views import BlogModelView

app_name = 'blog'

urlpatterns = [
    path('', BlogModelView.as_view(), name='blogs')
]