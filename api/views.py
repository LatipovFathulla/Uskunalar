from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from about.models import AboutModel
from api.serializer import BannerInfoModelSerializer, LinesModelSerializer, BiznesModelSerializer, VideoModelSerializer, \
    BlogModelSerializer, AboutModelSerializer, GalleryModelSerializer, WorkModelSerializer, CarouselSerializer, \
    CategorySerializer, SubCategorySerializer, PartnerSerializer, LineCategoryModelSerializer
from biznes.models import BiznesModel
from blog.models import BlogModel
from clients.models import ClientModel
from gallery.models import GalleryModel
from home.models import BannerInfoModel, CarouselModel, CategoryModel, SubCategoryModel
from lines.models import LineModel, LineCategoryModel
from videos.models import VideoModel
from works.models import WorkModel


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 0
    page_size_query_param = 'page_size'
    max_page_size = 1000


class NullStandardResultsSetPagination(PageNumberPagination):
    page_size = 0
    page_size_query_param = 'page_size'
    max_page_size = 0

class BannerInfoModelAPIView(ListAPIView):
    queryset = BannerInfoModel.objects.all()
    serializer_class = BannerInfoModelSerializer


class ALLBannerInfoModelAPIView(ListAPIView):
    queryset = BannerInfoModel.objects.all()
    serializer_class = BannerInfoModelSerializer
    pagination_class = StandardResultsSetPagination


class BannerDetailAPIView(APIView):
    def get(self, request, pk):
        products = BannerInfoModel.objects.get(pk=pk)
        serializer = BannerInfoModelSerializer(products, context={'request': request})
        return Response(serializer.data)


class LinesInfoModelAPIView(ListAPIView):
    queryset = LineModel.objects.all()
    serializer_class = LinesModelSerializer
    pagination_class = NullStandardResultsSetPagination


class LinesCategoriesAPIView(ListAPIView):
    queryset = LineCategoryModel.objects.all()
    serializer_class = LineCategoryModelSerializer


class LinesDetailAPIView(APIView):
    def get(self, request, pk):
        products = LineModel.objects.get(pk=pk)
        serializer = LinesModelSerializer(products, context={'request': request})
        return Response(serializer.data)


class BiznesInfoModelAPIView(ListAPIView):
    queryset = BiznesModel.objects.all()
    serializer_class = BiznesModelSerializer
    pagination_class = NullStandardResultsSetPagination


class BiznesDetailAPIView(APIView):
    def get(self, request, pk):
        products = BiznesModel.objects.get(pk=pk)
        serializer = BiznesModelSerializer(products, context={'request': request})
        return Response(serializer.data)


class VideoInfoModelAPIView(ListAPIView):
    queryset = VideoModel.objects.all()
    serializer_class = VideoModelSerializer
    pagination_class = NullStandardResultsSetPagination


class VideoDetailAPIView(APIView):
    def get(self, request, pk):
        products = VideoModel.objects.get(pk=pk)
        serializer = VideoModelSerializer(products, context={'request': request})
        return Response(serializer.data)


class BlogInfoModelAPIView(ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer
    pagination_class = NullStandardResultsSetPagination


class BlogDetailAPIView(APIView):
    def get(self, request, pk):
        products = BlogModel.objects.get(pk=pk)
        serializer = BlogModelSerializer(products, context={'request': request})
        return Response(serializer.data)


class AboutInfoModelAPIView(ListAPIView):
    queryset = AboutModel.objects.all()
    serializer_class = AboutModelSerializer
    pagination_class = NullStandardResultsSetPagination


class AboutDetailAPIView(APIView):
    def get(self, request, pk):
        products = AboutModel.objects.get(pk=pk)
        serializer = AboutModelSerializer(products, context={'request': request})
        return Response(serializer.data)


class GalleryInfoModelAPIView(ListAPIView):
    queryset = GalleryModel.objects.all()
    serializer_class = GalleryModelSerializer
    pagination_class = NullStandardResultsSetPagination


class GalleryDetailAPIView(APIView):
    def get(self, request, pk):
        products = GalleryModel.objects.get(pk=pk)
        serializer = GalleryModelSerializer(products, context={'request': request})
        return Response(serializer.data)


class WorkInfoModelAPIView(ListAPIView):
    queryset = WorkModel.objects.all()
    serializer_class = WorkModelSerializer
    pagination_class = NullStandardResultsSetPagination


class WorkDetailAPIView(APIView):
    def get(self, request, pk):
        products = WorkModel.objects.get(pk=pk)
        serializer = WorkModelSerializer(products, context={'request': request})
        return Response(serializer.data)


class BannerCarouselAPIView(ListAPIView):
    queryset = CarouselModel.objects.all()
    serializer_class = CarouselSerializer
    pagination_class = StandardResultsSetPagination


class CategoryAPIView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination
    #
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     categories_counts = queryset.order_by().values('category').annotate(
    #         count=Count('*')
    #     )
    #     return Response({
    #         d['category']: d['count']
    #         for d in categories_counts
    #     })


class SubCategoryAPIView(ListAPIView):
    queryset = SubCategoryModel.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = StandardResultsSetPagination


class PartnersAPIView(ListAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = PartnerSerializer
    pagination_class = StandardResultsSetPagination
