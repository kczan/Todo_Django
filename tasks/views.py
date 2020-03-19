from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required


@login_required
def list_homepage(request):
    tasks = Task.objects.all()

    for task in tasks:
        if "['" and "']" in task.title:
            task.title = task.title[2:-2]       # CharField returns a string that is looking like one-element list. Have no idea why yet.
                                                # try using form instead of modelform.
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm({**request.POST, **{'author': request.user.username}})
        if form.is_valid():
            form.clean()
            # form = form.cleaned_data
            form.save()
            print(form.cleaned_data)
        else:
            print(form.errors)
        return redirect('/list/home')

    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {
        'page_title': 'Todo list',
        'tasks': tasks,
        'form': form,
        'username': username,
    }
    return render(request, 'tasks/list.html', context)


@login_required
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('../..')
    context = {
        'form': form,
        'page_title': 'Update task',
    }
    return render(request, 'tasks/update_task.html', context)


@login_required
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
