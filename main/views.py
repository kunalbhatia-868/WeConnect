from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from main import models
# Create your views here.

class Wall(LoginRequiredMixin,ListView):
    template_name="main/wall.html"
    context_object_name="feed"
    login_url="login"

    def get_queryset(self):
        friendIds=[friend.person2.id for friend in models.Friend.objects.filter(person1=self.request.user)]
        friendIds+=[friend.person1.id for friend in models.Friend.objects.filter(person2=self.request.user)]
        
        return models.Post.objects.filter(user__in=friendIds)

class Home(LoginRequiredMixin,ListView):
    template_name='main/home.html'
    context_object_name="posts"
    login_url="login"

    def get_queryset(self):
        return models.Post.objects.filter(user=self.request.user)
    