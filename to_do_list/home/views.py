from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from home.models import Task

@login_required(login_url='login')
def home(request):
    context = {'saved': False}
    if request.method == 'POST':
        title = request.POST['title']
        print(title)
        ins = Task(title=title)
        ins.save()
        context = {'saved': True}
    allTasks = Task.objects.filter(user=request.user)
    context['tasks'] = allTasks

    return render(request, 'index.html', context)

@login_required(login_url='login')
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id, user=request.user)
    task.delete()
    return redirect('home')