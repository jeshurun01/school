from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'Structurer le project',
        'text': 'Etablir toute la structure de notre projet. Je dois faire un croquis à main lever'
    }
    return render(request, 'main/index.html', context)
