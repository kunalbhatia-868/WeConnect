from django.urls import path
from main import views


urlpatterns=[
    path('',views.Wall.as_view(),name="wall"),
    path('home/',views.Home.as_view(),name="home"),    
    path('create/',views.CreatePost.as_view(),name="create_post"),
    path('friends/',views.Friends.as_view(),name="friends"),
    path('friends/<int:pk>/',views.UserDetail.as_view(),name="friend_detail"),
    path('post/<int:pk>/comment/',views.PostComment.as_view(),name="create_comment")
]