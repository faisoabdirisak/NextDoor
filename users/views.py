# from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreation
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def loginUser(request):
    page='login'

    if request.user.is_authenticated:
        return redirect('neighbors')
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)

        except:
            messages.error(request,'Username does not exist')    

        user=authenticate(request,username=username, password=password)   

        if user is not None:
            login(request,user)
            return redirect('neighbors') 
        else:
              messages.error(request,"user name or password is incorrect")    

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, "User wa successfullt logout")    
    return redirect('login')


def registerUser(request):
    page='register'
    form=CustomUserCreation()

    if request.method =='POST':
        form =CustomUserCreation(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()

            messages.success(request,'User account wa created')

            login(request,user)
            return redirect('neighbors')

        else:
             messages.error(request,'registration not successfully')


    context={'page':page,'form':form}
    return render(request, 'users/login_register.html',context)

def profiles(request):
    profiles=Profile.objects.all()
    context={ 'profiles':profiles}
    return render(request, 'users/profiles.html',context)

def userProfile(request,pk):
    profile=Profile.objects.get(id=pk)
    context={'profile':profile}
    return render(request, 'users/user-profile.html',context)    



