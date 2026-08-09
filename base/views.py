from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
# Create your views here.
from .form import *

def index(request):
    tasks= Task.objects.all()
    completed_task= Task.objects.filter(complete=True).count()
    incomplete_task= Task.objects.filter(complete=False).count()
    form= TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    context={
        'tasks':tasks,
        'form': form,
        'completed_task': completed_task,
        'incomplete_task': incomplete_task
    }
    return render(request, 'base/list.html', context)

def updateTask(request,pk):
    task= Task.objects.get(id=pk)
    form=  TaskForm(instance=task)

    if request.method == 'POST':
        form=  TaskForm(request.POST, instance=task)
        if form.is_valid:
         form.save()
         return redirect("/")
        
    context={
        'form':form,
        'task':task
    }
    return render(request, 'base/update_task.html', context)

def deleteTask(request, pk):
    task= Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    context={
        'task':task
    }
    return render(request, 'base/delete_task.html',context)

