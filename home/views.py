import django
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth  import authenticate,  login, logout


# Create your views here.

def home(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def log(request):
    return render(request,'login.html')


def handleSign(request):
    print(request)
    if request.method=="POST":
        
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        password=request.POST['password']

        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        print(user)
        if user is not None:
            login(request, user)
            # messages.success(request, "Successfully Logged In")
            # return redirect("home")
            return redirect("home")

        else:
            messages.error(request, "Invalid credentials! Please try again")
            print(user)
            return redirect("home")

    return HttpResponse("404- Not found")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def contact(request):
    return render(request,"contact.html")