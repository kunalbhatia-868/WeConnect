from django.shortcuts import render
from django.views.generic import ListView
from main import models
# Create your views here.

class Wall(ListView):
    template_name="main/wall.html"
    context_object_name="feed"

    def get_queryset(self):
        friendIds=[friend.person2.id for friend in models.Friend.objects.filter(person1=self.request.user)]
        friendIds+=[friend.person1.id for friend in models.Friend.objects.filter(person2=self.request.user)]
        
        return models.Post.objects.filter(user__in=friendIds)

class Home(ListView):
    template_name='main/home.html'
    context_object_name="posts"

    def get_queryset(self):
        return models.Post.objects.filter(user=self.request.user)
    