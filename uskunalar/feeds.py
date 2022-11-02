from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from home.models import BannerInfoModel


class LatestPostsFeed(Feed):
    title = 'My product'
    link = '/products2/'
    description = 'New product of my blog.'


    def items(self):
        return BannerInfoModel.objects.all()[:1]


def item_title(self, item):
    return item.title


def item_description(self, item):
    return truncatewords(item.long_description, 30)
