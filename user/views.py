from django.shortcuts import render,redirect
import requests
import json
from django.contrib import messages
from django.contrib.auth import login as auth_login , authenticate, logout as auth_logout
from rest_framework.authtoken.models import Token

# Registration View Template Rendering
def registration(request):
    if request.method == "POST":
        content = requests.post(url='http://127.0.0.1:8000/user/api/register/', data=request.POST)
        if content.status_code == 201:
            messages.success(request, "Please Check your Email")
            return redirect('login')
        
    return render(request,'user/registration.html')


# Login Rendering
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            password = request.POST['password']
            username = request.POST['username']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
            data = {}
            data['username'] = request.POST["username"]
            data['password'] = request.POST["password"]
            content = requests.post(url="http://127.0.0.1:8000/user/api/login/", data=data)
            # content = content.json()
            print(content)
            if content == 200:
                return redirect('/')
            return render(request,'user/login.html',{'content':content})
        return render(request,'user/login.html')

        
#Logout View 
def logout(request):
    if request.user.is_authenticated:
        user = request.user
        token = Token.objects.get(user=user)
        headers = {'Authorization':f"Token {token}"}
        url = "http://127.0.0.1:8000/user/api/logout/"
        response = requests.get(url=url, headers=headers)
        auth_logout(request)
        return redirect("login")
    else:
        return redirect('login')
    
# Reset Password
def get_reset_password(request):
    if request.method == "POST":
        content = requests.post(url="http://127.0.0.1:8000/user/api/password_reset/", data=request.POST)
        print(content)
        if content.status_code == 200:
            messages.success(request, "Please Check your Email")
        else:
            messages.error(request, "Please Enter a valid Email")
    return render(request, 'user/reset_password.html')

# New Password Set View 
def reset_password(request,token):
    data = {}
    if request.method == "POST":
        data['password'] = request.POST['password']
        data['token'] = token 
        content = requests.post(url="http://127.0.0.1:8000/user/api/password_reset/confirm/", data=data)
        data = content.json()

        if content.status_code == 200:
            messages.success(request, "Your Password Reset Successful!")
            redirect('login')
        return render(request, 'user/set_new_password.html',{'data':data})
    return render(request, 'user/set_new_password.html')