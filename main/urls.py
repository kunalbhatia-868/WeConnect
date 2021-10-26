from django.urls import path
from main import views


urlpatterns=[
    path('',views.Wall.as_view(),name="wall"),
    path('home',views.Home.as_view(),name="home"),    
]