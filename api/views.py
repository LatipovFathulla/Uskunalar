from django.shortcuts import render
from rest_framework.generics import ListAPIView

from api.serializer import BannerInfoModelSerializer
from home.models import BannerInfoModel


class BannerInfoModelAPIView(ListAPIView):
    queryset = BannerInfoModel.objects.all()
    serializer_class = BannerInfoModelSerializer
