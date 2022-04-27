from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from boot.models import Inquiry

# Create your views here.


def test(request):
    return render(request,"base.html")

def blog(request):
    if not request.user.is_authenticated:
        return redirect("boot:login")
    return render(request,"boot/blog.html")

def about(request):
    return render(request,"boot/about.html")

def contact(request):
    return render(request,"boot/contact.html")

def home(request):
    print(request.user.is_authenticated)
    return render(request,"boot/home.html")

def inquiry_create(request):
    if request.method=="POST":
        fullname=request.POST.get("fullname")
        email_adress = request.POST.get("email_adress")
        phone_number = request.POST.get("phone_number")
        message = request.POST.get("message")
        new_inquiry=Inquiry()
        new_inquiry.fullname=fullname
        new_inquiry.email_adress=email_adress
        new_inquiry.phone_number=phone_number
        new_inquiry.message=message
        new_inquiry.save()

    return redirect("boot:contact")


def login(request):
    if request.user.is_authenticated:
        return redirect("boot:home")
    context={}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(
            request, 
            username=username, 
            password=password
        )
        if user is not None:
            auth.login(request, user)
            return redirect("boot:home")

    return render(request,"boot/login.html", context=context)

def sign_up(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_check = request.POST.get("password_check")
        if username is not None and password is not None and password_check ==password_check :
            new_user=User.objects.create_user(
                username=username,
                password=password,
            )
            return redirect ("boot:home")
        

    return render(request,"boot/sign-up.html")

def logout(request):
    print(request.user.is_authenticated)
    if request.method =="POST":
        auth.logout(request)

    return redirect("boot:home")