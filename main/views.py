from django.shortcuts import redirect, render
from django.views.generic import ListView,CreateView
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
        
        return models.Post.objects.filter(user__in=friendIds)

    def get_context_data(self, **kwargs):
        context_data=super().get_context_data(**kwargs)
        context_data['form']=forms.PostForm
        return context_data    

class Home(LoginRequiredMixin,ListView):
    template_name='main/home.html'
    context_object_name="posts"
    login_url="login"

    def get_queryset(self):
        return models.Post.objects.filter(user=self.request.user)
    

class CreatePost(CreateView):
    def post(self,request):
        form=forms.PostForm(request.POST,request.FILES)
        if form.is_valid():
            post_form=form.save(commit=False)
            post_form.user=self.request.user
            post_form.save()
            return redirect('wall')
        else:
            messages.info(f" Please Enter valid Entries")
        
    
