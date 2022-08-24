from django.shortcuts import render
from django.views.generic import ListView

from clients.models import ClientModel


class ClientModelView(ListView):
    template_name = 'index.html'
    model = ClientModel

    def get_queryset(self):
        pass
