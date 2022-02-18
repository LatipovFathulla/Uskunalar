from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from videos.models import VideoModel


class VideoListView(ListView):
    template_name = 'videos.html'
    queryset = VideoModel.objects.order_by('-pk')
    paginate_by = 3
    context_object_name = 'videos'


def get_success_url():
    return reverse('video:videos')
