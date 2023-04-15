from django.shortcuts import render, redirect

from .models import Task
from .forms import CreateTaskForm


def index(request):
    tasks = Task.objects.all()

    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'list.html', context)
