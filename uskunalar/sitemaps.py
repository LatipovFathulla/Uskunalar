from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from about.models import AboutModel
from biznes.models import BiznesModel
from home.models import BannerInfoModel


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return BannerInfoModel.objects.all()

    def lastmod(self, obj):
        return obj.created_at


class AboutSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return AboutModel.objects.all()

    def lastmod(self, obj):
        return obj.created_at


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home:about', 'home:contacts', 'biznes:biznes']

    def location(self, item):
        return reverse(item)


class BiznesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return BiznesModel.objects.all()

    def lastmod(self, obj):
        return obj.created_at
