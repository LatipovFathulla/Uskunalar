from django.shortcuts import render
from rest_framework.generics import ListAPIView

from about.models import AboutModel
from api.serializer import BannerInfoModelSerializer, LinesModelSerializer, BiznesModelSerializer, VideoModelSerializer, \
    BlogModelSerializer, AboutModelSerializer, GalleryModelSerializer, WorkModelSerializer
from biznes.models import BiznesModel
from blog.models import BlogModel
from gallery.models import GalleryModel
from home.models import BannerInfoModel
from lines.models import LineModel
from videos.models import VideoModel
from works.models import WorkModel


class BannerInfoModelAPIView(ListAPIView):
    queryset = BannerInfoModel.objects.all()
    serializer_class = BannerInfoModelSerializer


class LinesInfoModelAPIView(ListAPIView):
    queryset = LineModel.objects.all()
    serializer_class = LinesModelSerializer


class BiznesInfoModelAPIView(ListAPIView):
    queryset = BiznesModel.objects.all()
    serializer_class = BiznesModelSerializer


class VideoInfoModelAPIView(ListAPIView):
    queryset = VideoModel.objects.all()
    serializer_class = VideoModelSerializer


class BlogInfoModelAPIView(ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer


class AboutInfoModelAPIView(ListAPIView):
    queryset = AboutModel.objects.all()
    serializer_class = AboutModelSerializer


class GalleryInfoModelAPIView(ListAPIView):
    queryset = GalleryModel.objects.all()
    serializer_class = GalleryModelSerializer


class WorkInfoModelAPIView(ListAPIView):
    queryset = WorkModel.objects.all()
    serializer_class = WorkModelSerializer
