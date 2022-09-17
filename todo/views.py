from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView

from profiles.models import Profile
from .forms import TaskForm
from .models import Task


@login_required
def add_task(request):
    template_name = 'todo/add_task.html'
    context = {}
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            author = Profile.objects.get(user=request.user)
            task.author = author
            task.save()
            return redirect('main:home')

    context['form'] = form

    return render(request, template_name, context)


@login_required
def edit_task(request, slug):
    template_name = 'todo/edit_task.html'
    task = Task.objects.get(slug=slug)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('main:home')

    return render(request, template_name, {'form': form})


@login_required
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('main:home')


class TaskDetail(DetailView):
    template_name = 'todo/task_detail.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
