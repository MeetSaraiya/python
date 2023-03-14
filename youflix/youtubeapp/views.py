from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from .models import Youtuber

# Create your views here.
def index(request):
    return render(request,'youtubeapp/index.html')

def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        cpass=request.POST['cpassword']
        if cpass != password:
            messages.warning(request,'''Password is not matching''')
            # print(username,email,password,cpass)
            return redirect("signup")
#username:admin
#password:02580258
        else:
            if email and username and password:
                a=User.objects.create_user(username,email,password)
                if a:
                    messages.success(request,'''You are part of our family,now login with your details''')
                    return redirect('login')
             
    return render(request,'youtubeapp/signup.html')
    
 

def login1(request):
    if request.method=="POST":
        uname=request.POST['username']
        pword=request.POST['password']
        user=authenticate(username=uname,password=pword)
        if user:
            login(request,user)
            return redirect('index')
        else:
            messages.warning(request,'''Please create account or provided details are wrong''')
            return redirect('login')
    return render(request,'youtubeapp/login.html')
    
def youtuber(request):
    check=  Youtuber.objects.filter(youtuber=request.user)
    if not check:
        youtuber=Youtuber.objects.create(youtuber=request.user)
        if youtuber:
            return redirect("uploadvideo") 
        
    else:
        return redirect('index')
    

    return HttpResponse("youtuber created")

def videoupload(request):
    pass


def video(request):
    pass

def create_channel(request):
    return render(request,'youtubeapp/createchannel.html')