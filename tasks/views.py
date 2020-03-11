from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.


def list_homepage(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('/list/home')

    context = {
        'page_title': 'Todo list',
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'tasks/list.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
        'page_title': 'Update task',
    }
    return render(request, 'tasks/update_task.html', context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/list')

    context = {
        'page_title': 'Delete task',
        'task': task,
    }

    return render(request, 'tasks/delete_task.html', context)