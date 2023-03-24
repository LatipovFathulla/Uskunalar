from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include, re_path
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from .yasg import urlpatterns as doc_urls
from home.models import BannerInfoModel
from uskunalar.feeds import LatestPostsFeed
from uskunalar.sitemaps import PostSitemap, AboutSitemap, StaticViewSitemap, BiznesSitemap, LinesSitemap, WorksSitemap, \
    BlogSitemap

info_dict = {
    'queryset': BannerInfoModel.objects.all(),
}

sitemaps = {
    # 'about': AboutSitemap,
    'biznes': BiznesSitemap,
    'lines': LinesSitemap,
    'works': WorksSitemap,
    'blogs': BlogSitemap,
}

product_sitemaps = {
    'posts': PostSitemap,
}

all_sitemaps = {
    'biznes': BiznesSitemap,
    'lines': LinesSitemap,
    'works': WorksSitemap,
    'blogs': BlogSitemap,
    'posts': PostSitemap,
}

urlpatterns = [
    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('sitemap.xml', sitemap,
         {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'
         ),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('api-auth/', include('api.urls')),
    path('sitemap2.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('sitemap_products_2.xml', sitemap, {'sitemaps': product_sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('all_sitemaps.xml', sitemap, {'sitemaps': all_sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
)

urlpatterns += doc_urls

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
#
# handler404 = "about.views.handle_not_found"

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
