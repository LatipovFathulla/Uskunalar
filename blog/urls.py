from django.urls import path

from blog.views import BlogModelView, SingleBlogView

app_name = 'blog'

urlpatterns = [
    path('', BlogModelView.as_view(), name='blogs'),
    path('single-blog/', SingleBlogView.as_view(), name='single-blog')
]