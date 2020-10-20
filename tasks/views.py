from django.shortcuts import render, redirect
from .models import *

def task(request):
    task = Task.objects.all().order_by('-date_created')
    return render(request,'crm/task.html',{'task':task})

def add_task(request):
    if request.method == 'POST':
        tname = request.POST.get('task_name')
        tdesc = request.POST.get('task_desc')
        if (tname != ""):
            task = Task.objects.create(name=tname,desc=tdesc)
            task.save()
    return redirect('/task')

def del_task(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/task')