from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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


class BannerDetailAPIView(APIView):
    def get(self, request, pk):
        products = BannerInfoModel.objects.get(pk=pk)
        serializer = BannerInfoModelSerializer(products, context={'request': request})
        return Response(serializer.data)


class LinesInfoModelAPIView(ListAPIView):
    queryset = LineModel.objects.all()
    serializer_class = LinesModelSerializer


class LinesDetailAPIView(APIView):
    def get(self, request, pk):
        products = LineModel.objects.get(pk=pk)
        serializer = LinesModelSerializer(products, context={'request': request})
        return Response(serializer.data)


class BiznesInfoModelAPIView(ListAPIView):
    queryset = BiznesModel.objects.all()
    serializer_class = BiznesModelSerializer


class BiznesDetailAPIView(APIView):
    def get(self, request, pk):
        products = BiznesModel.objects.get(pk=pk)
        serializer = BiznesModelSerializer(products, context={'request': request})
        return Response(serializer.data)


class VideoInfoModelAPIView(ListAPIView):
    queryset = VideoModel.objects.all()
    serializer_class = VideoModelSerializer


class VideoDetailAPIView(APIView):
    def get(self, request, pk):
        products = VideoModel.objects.get(pk=pk)
        serializer = VideoModelSerializer(products, context={'request': request})
        return Response(serializer.data)


class BlogInfoModelAPIView(ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer


class BlogDetailAPIView(APIView):
    def get(self, request, pk):
        products = BlogModel.objects.get(pk=pk)
        serializer = BlogModelSerializer(products, context={'request': request})
        return Response(serializer.data)


class AboutInfoModelAPIView(ListAPIView):
    queryset = AboutModel.objects.all()
    serializer_class = AboutModelSerializer


class AboutDetailAPIView(APIView):
    def get(self, request, pk):
        products = AboutModel.objects.get(pk=pk)
        serializer = AboutModelSerializer(products, context={'request': request})
        return Response(serializer.data)


class GalleryInfoModelAPIView(ListAPIView):
    queryset = GalleryModel.objects.all()
    serializer_class = GalleryModelSerializer


class GalleryDetailAPIView(APIView):
    def get(self, request, pk):
        products = GalleryModel.objects.get(pk=pk)
        serializer = GalleryModelSerializer(products, context={'request': request})
        return Response(serializer.data)


class WorkInfoModelAPIView(ListAPIView):
    queryset = WorkModel.objects.all()
    serializer_class = WorkModelSerializer


class WorkDetailAPIView(APIView):
    def get(self, request, pk):
        products = WorkModel.objects.get(pk=pk)
        serializer = WorkModelSerializer(products, context={'request': request})
        return Response(serializer.data)
