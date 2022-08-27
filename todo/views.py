from django.shortcuts import render, redirect

from profiles.models import Profile
from .forms import TaskForm
from .models import Task


def add_task(request):
    template_name = 'todo/add_task.html'
    context = {}
    user_id = request.user.id
    if user_id is not None:
        form = TaskForm()
        if request.method == 'POST':
            print(request.POST)
            form = TaskForm(request.POST)
            if form.is_valid():
                author = Profile.objects.get(user=request.user)
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                task_done = form.cleaned_data['task_done']
                task = Task(author=author, title=title, description=description, task_done=task_done)
                task.save()
                return redirect('main:home')

        context['form'] = form

    return render(request, template_name, context)
