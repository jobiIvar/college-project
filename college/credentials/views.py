from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home:home")
        else:
            messages.info(request, "Username or password is invalid")
            return redirect("credentials:signin")

    return render(request, 'signin.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        c_password = request.POST['password1']
        if (not username) or (not email) or (not password):
            messages.warning(request,"Enter all the details....")
        elif password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect("credentials:signup")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect("credentials:signup")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, "User Created")
                user.save()

                return redirect("credentials:signin")
    return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect("home:home")
