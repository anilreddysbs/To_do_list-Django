from django.shortcuts import render,redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            return redirect('task_list')  # Redirect to the task list page after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def task_list(request):
    query = request.GET.get('q', '')  # Get search input
    status_filter = request.GET.get('status', '')  # Get status filter
    tasks = Task.objects.filter(user=request.user)  # Show only user's tasks

    if query:
        tasks = tasks.filter(title__icontains=query)  # Case-insensitive search in task titles
    
    if status_filter:
        tasks = tasks.filter(status__icontains=status_filter)  # Filter by exact status

    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == "POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        due_date=request.POST.get('due_date')
        if due_date:
            task=Task.objects.create(title=title,description=description,due_date=due_date,user=request.user)
        else:
            task=Task.objects.create(title=title,description=description,user=request.user)
        task.save()
        return redirect('/')
    return render(request,'tasks/add_task.html')
@login_required
def delete_task(request,task_id):
    task=Task.objects.get(id=task_id,user=request.user)
    task.delete()
    return redirect('task_list')
@login_required
def complete_task(request,task_id):
    task=Task.objects.get(id=task_id,user=request.user)
    task.completed=True
    task.status='Completed'
    task.save()
    return redirect('task_list')