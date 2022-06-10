from django.urls import path
from django.views.decorators.cache import cache_page
from blog.views import BlogModelView, SingleBlogView

app_name = 'blog'

urlpatterns = [
    path('', cache_page(1800)(BlogModelView.as_view()), name='blogs'),
    path('<int:pk>/', cache_page(1800)(SingleBlogView.as_view()), name='single-blog')
]