from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from about.views import AboutModelListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('about.urls', namespace='home')),
    path('blogs/', include('blog.urls', namespace='blog')),
    path('works/', include('works.urls', namespace='work')),
    path('videos/', include('videos.urls', namespace='video')),
    path('lines/', include('lines.urls', namespace='line')),
    path('products/', include('home.urls', namespace='products'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
