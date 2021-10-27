from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import ListView,CreateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from main import models,forms
from django.contrib import messages
# Create your views here.

class Wall(LoginRequiredMixin,ListView):
    template_name="main/wall.html"
    context_object_name="feed"
    login_url="login"

    def get_queryset(self):
        friendIds=[friend.person2.id for friend in models.Friend.objects.filter(person1=self.request.user)]
        friendIds+=[friend.person1.id for friend in models.Friend.objects.filter(person2=self.request.user)]
        
        return models.Post.objects.filter(user__in=friendIds).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context_data=super().get_context_data(**kwargs)
        context_data['form']=forms.PostForm
        return context_data    

class Home(LoginRequiredMixin,ListView):
    template_name='main/home.html'
    context_object_name="posts"
    login_url="login"

    def get_queryset(self):
        return models.Post.objects.filter(user=self.request.user).order_by('-created_on')
    

class CreatePost(LoginRequiredMixin,CreateView):
    login_url='login'
    def post(self,request):
        form=forms.PostForm(request.POST,request.FILES)
        if form.is_valid():
            post_form=form.save(commit=False)
            post_form.user=self.request.user
            post_form.save()
            return redirect('wall')
        else:
            messages.info(f" Please Enter valid Entries")
        
    
class Friends(LoginRequiredMixin,ListView):
    template_name="main/friends.html"
    context_object_name="friends"
    login_url='login'

    def get_queryset(self):
        friendIds=[friend.person2 for friend in models.Friend.objects.filter(person1=self.request.user)]
        friendIds+=[friend.person1 for friend in models.Friend.objects.filter(person2=self.request.user)]
        return friendIds

class UserDetail(LoginRequiredMixin,DetailView):
    template_name="main/detail.html"
    model=User
    login_url='login'
