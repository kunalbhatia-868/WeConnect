from django.shortcuts import render
from django.views.generic import ListView
from main import models
# Create your views here.

class Wall(ListView):
    pass


class Home(ListView):
    template_name='main/home.html'
    context_object_name="posts"

    def get_queryset(self):
        return models.Post.objects.filter(user=self.request.user)
    