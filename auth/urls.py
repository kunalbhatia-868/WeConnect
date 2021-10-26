from django.urls import path
from auth import views

urlpatterns=[
    path('login/',views.logIn,name='login'),
    path('logout/',views.logOut,name='logout'),
    path('signup/',views.register,name='signup'),

]