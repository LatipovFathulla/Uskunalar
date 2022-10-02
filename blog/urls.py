from django.urls import path
from blog.views import BlogModelView, blog_view

app_name = 'blog'

urlpatterns = [
    path('', BlogModelView.as_view(), name='blogs'),
    path('<int:pk>/', blog_view, name='single-blog')
]