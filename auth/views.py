from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from auth.forms import SignUpForm
# Create your views here.

def logIn(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f"{user.username} has been logged in ")
        else:    
            messages.info(request,f"username or password didn't match")    

    return render(request,'auth/login.html')


def logOut(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method=='POST':
        form=SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,f"New Account has been created - {user} ")
        else:   
            messages.info(request,f"Please Enter Valid Details") 

    context={
        'form':SignUpForm,
    }
    return render(request,'auth/signup.html',context)