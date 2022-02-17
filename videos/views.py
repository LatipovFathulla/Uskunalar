from django.shortcuts import render
from django.views.generic import ListView

from videos.models import VideoModel


def index(request):
    videos = VideoModel.objects.order_by('-pk')
    return render(request, 'videos.html', context={'videos': videos})