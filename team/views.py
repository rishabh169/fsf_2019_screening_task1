from django.shortcuts import render, redirect
from .models import Task
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


def task_list(request):
    tasks = Task.objects.all().order_by('title')
    return render(request, 'team/task_list.html', {'tasks': tasks})


def task_detail(request, slug):
    task = Task.objects.get(slug=slug)
    return render(request, 'team/task_detail.html', {'task': task})


@login_required(login_url="/accounts/login/")
def task_create(request):
    if request.method == 'POST':
        form = forms.CreateTask(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('task:list')
    else:
        form = forms.CreateTask()
    return render(request, 'team/task_create.html', {'form': form})
