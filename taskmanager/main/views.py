from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'tasks': tasks })

def about(request):
    return render(request, 'main/about.html')

def registration(request):
    return render(request, 'main/registration.html')

def singIn(request):
    return render(request, 'main/singIn.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save();
            return redirect('main')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)