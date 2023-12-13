from django.shortcuts import render,redirect
from rest_framework.authtoken.models import Token
from .forms import TaskForm
import requests
import json

#Get Token
def get_token(request):
    if request.user.is_authenticated:
        token = Token.objects.get(user=request.user)
        headers = {"Authorization":f"Token {token}"}
        return headers
    else:
        return {}

# Task Template Show
def task_show(request):
    if request.user.is_authenticated:
        headers = get_token(request)
        context = requests.get("http://127.0.0.1:8000/api/manage/", headers=headers)
        context = context.json()
        
        return render(request,'task/home.html',{"context":context})
    else:
        return redirect('login')

# Add Task Form with Html template
def add_task(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            headers = get_token(request)
            # data = TaskForm(request.POST, request.FILES.getlist('upload_images'))
            data = {}
            data['title'] = TaskForm.cleaned_data['title']
            # print(data)
            response = requests.post('http://127.0.0.1:8000/api/manage/',data=data, headers=headers)
            print(response.json())
            if response.status_code == 201:
                return redirect('/')
        form = TaskForm()
        context = {
            'form':form
        }
        return render(request,'task/add_task_copy.html', context)
    else:
        return redirect("login")
    
# Complete Task With Html Template
def completed(request,pk):
    if request.user.is_authenticated:
        headers = get_token(request)
        data = {}
        data['complete'] = True
        json_data = json.dumps(data)
        context = requests.patch(f"http://127.0.0.1:8000/api/update/{pk}/",headers=headers,data=json_data)
        print(context.json())
        return redirect('/')
    else:
        return redirect('/')

# Delete Task
def delete_task(request,pk):
    if request.user.is_authenticated:
        headers = get_token(request)
        context = requests.delete((f"http://127.0.0.1:8000/api/manage/{pk}"),headers=headers)
        return redirect('/')
    else:
        return redirect('/')

# Search View
def Searching(request):
    if request.user.is_authenticated:
        headers = get_token(request)
        search = request.GET['search']
        url = "http://127.0.0.1:8000/api/manage/?search={}".format(search)
        res = requests.get(url=url,headers=headers)
        res = res.json()
        context ={
            "context":res,
            'search':search
        }
        return render(request, 'task/home.html', context)
    else:
        return redirect('/')

# Filter View
def filtering(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            created_date = ""
            start_date = ""
            end_date = ""
            priority = ""
            complete = True
            url = "http://127.0.0.1:8000/api/manage/?create_date={}&start_date={}&end_date={}&priority={}&complete={}".format(created_date, start_date, end_date, priority, complete)
            headers = get_token(request)
            res = requests.get(url=url, headers=headers)
            res = res.json()
            context = {
                'context':res,
                "created_date":created_date,
                "end_date":end_date,
                'start_date':start_date,
                'priority' : priority,
                'complete' : complete
            }

            return render(request,'task/home.html',context)
    else:
        return redirect('/')
