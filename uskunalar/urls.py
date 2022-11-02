from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include, re_path
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from about.views import HomeView
from home.views import CategoryTest, get_subcategory

from home.models import BannerInfoModel
from uskunalar.feeds import LatestPostsFeed
from uskunalar.sitemaps import PostSitemap, AboutSitemap, StaticViewSitemap, BiznesSitemap

info_dict = {
    'queryset': BannerInfoModel.objects.all(),
}

sitemaps = {
    'about': AboutSitemap,
    'statics': StaticViewSitemap,
    'posts': PostSitemap,
    'biznes': BiznesSitemap,
}

urlpatterns = [
    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('sitemap.xml', sitemap,
         {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'
         ),

    path('sitemap2.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='index'),
    path('', include('about.urls', namespace='home')),
    path('blogs/', include('blog.urls', namespace='blog')),
    path('works/', include('works.urls', namespace='work')),
    path('gallery/', include('gallery.urls', namespace='galleries')),
    path('videos/', include('videos.urls', namespace='video')),
    path('lines/', include('lines.urls', namespace='line')),
    path('biznes/', include('biznes.urls', namespace='biznes')),
    path('products/', include('home.urls', namespace='products')),
    path('test/', CategoryTest.as_view()),
    path('api-auth/', include('api.urls')),
    path('getSubcategory/', get_subcategory, name='subcategory'),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
#
# handler404 = "about.views.handle_not_found"

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
