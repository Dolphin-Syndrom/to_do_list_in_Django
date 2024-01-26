from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    context = {'saved': False}
    if request.method == 'POST':
        title = request.POST['title']
        print(title)
        ins = Task(title=title)
        ins.save()
        context = {'saved': True}
    allTasks = Task.objects.all()
    context['tasks'] = allTasks

    return render(request, 'index.html', context)

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('home')