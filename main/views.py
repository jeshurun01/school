from django.shortcuts import render
from django.contrib.auth import authenticate, update_session_auth_hash
from profiles.models import Profile
from todo.models import Task


# Create your views here.
def index(request):

    user = request.user.id
    if user is not None:
        profile = Profile.objects.get(user=request.user)
        tasks = Task.objects.filter(author=profile)
        context = {
            'tasks': tasks[::-1],
            'profile': profile,
        }
    else:
        context = {}
    return render(request, 'main/index.html', context)
