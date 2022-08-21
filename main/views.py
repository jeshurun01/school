from django.shortcuts import render
from user_profile.models import Profile


# Create your views here.
def index(request):
    profile = Profile.objects.get(pk=2)
    context = {
        'title': 'Structurer le project',
        'text': 'Etablir toute la structure de notre projet. Je dois faire un croquis à main lever',
        'profile': profile,
    }
    return render(request, 'main/index.html', context)
