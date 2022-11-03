from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from about.models import AboutModel
from biznes.models import BiznesModel
from blog.models import BlogModel
from home.models import BannerInfoModel
from lines.models import LineModel
from works.models import WorkModel


class PostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return BannerInfoModel.objects.all()

    def lastmod(self, obj):
        return obj.created_at


class AboutSitemap(Sitemap):
    pass
    # changefreq = 'weekly'
    # priority = 0.9
    #
    # def items(self):
    #     return AboutModel.objects.all()
    #
    # def lastmod(self, obj):
    #     return obj.created_at


class StaticViewSitemap(Sitemap):
    pass
    # def items(self):
    #     return ['home:about', 'home:contacts', 'biznes:biznes']
    #
    # def location(self, item):
    #     return reverse(item)


class BiznesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return BiznesModel.objects.all()

    def lastmod(self, obj):
        return obj.created_at


class LinesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return LineModel.objects.all()

    def lastmod(self, obj):
        return obj.created_at


class WorksSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return WorkModel.objects.all()

    def lastmod(self, obj):
        return obj.created_at


class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return BlogModel.objects.all()

    def lastmod(self, obj):
        return obj.created_at
