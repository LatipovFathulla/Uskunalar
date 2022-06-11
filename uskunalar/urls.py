from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from home.views import CategoryTest, get_subcategory

urlpatterns = [
    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('about.urls', namespace='home')),
    path('blogs/', include('blog.urls', namespace='blog')),
    path('works/', include('works.urls', namespace='work')),
    path('videos/', include('videos.urls', namespace='video')),
    path('lines/', include('lines.urls', namespace='line')),
    path('biznes/', include('biznes.urls', namespace='biznes')),
    path('products/', include('home.urls', namespace='products')),
    path('test/', CategoryTest.as_view()),
    path('getSubcategory/', get_subcategory, name='subcategory')
)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
