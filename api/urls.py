from api.views import BannerInfoModelAPIView, LinesInfoModelAPIView, BiznesInfoModelAPIView, VideoInfoModelAPIView, \
    BlogInfoModelAPIView, AboutInfoModelAPIView, GalleryInfoModelAPIView, WorkInfoModelAPIView
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('products/', BannerInfoModelAPIView.as_view(), name='products'),
    path('lines/', LinesInfoModelAPIView.as_view(), name='lines'),
    path('biznes/', BiznesInfoModelAPIView.as_view(), name='biznes'),
    path('videos/', VideoInfoModelAPIView.as_view(), name='videos'),
    path('blogs/', BlogInfoModelAPIView.as_view(), name='blogs'),
    path('abouts/', AboutInfoModelAPIView.as_view(), name='abouts'),
    path('galleries/', GalleryInfoModelAPIView.as_view(), name='galleries'),
    path('works/', WorkInfoModelAPIView.as_view(), name='works'),
]