from django.shortcuts import render
from profiles.models import Profile


# Create your views here.
def index(request):
    profile = Profile.objects.all()
    print(len(profile))
    context = {
        'title': 'Structurer le project',
        'text': 'Etablir toute la structure de notre projet. Je dois faire un croquis à main lever',
        'profile': profile[1] if profile else "None",
    }
    return render(request, 'main/index.html', context)
