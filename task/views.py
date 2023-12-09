from django.shortcuts import render,redirect
from rest_framework.authtoken.models import Token
from .forms import TaskForm
import requests
import json

# Task Template Show
def task_show(request):
    # token = Token.objects.get(user=request.user)
    # print(token)
    context = requests.get("http://127.0.0.1:8000/api/manage/")
    context = context.json()
    
    return render(request,'task/home.html',{"context":context})

# Add Task Form with Html template
def add_task(request):
    if request.method == 'POST':
        token = Token.objects.get(user=request.user)
        headers = {'Authorization': f"Token {token}"}
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

# Complete Task With Html Template
def completed(request,pk):
    res = requests.get(f"http://127.0.0.1:8000/api/manage/{pk}/").json()
    data = {}
    data['user'] = res['user']
    data['title'] = res['title']
    data['description'] = res['description']
    data['start_date'] = res['start_date']
    data['end_date'] = res['end_date']
    data['image'] = str(res['image'])
    data['priority'] = res['priority']
    data['complete'] = True
    json_data = json.dumps(data)
    print(type(res['image']))
    headers = {'content-type':'application/json'}
    context = requests.put(f"http://127.0.0.1:8000/api/manage/{pk}/",headers=headers,data=json_data)
    print(context)
    return redirect('/')

# Delete Task
def delete_task(request,pk):
    context = requests.delete((f"http://127.0.0.1:8000/api/manage/{pk}"))
    return redirect('/')
