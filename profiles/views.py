from django.shortcuts import render, redirect

from profiles.forms import NewUserForm


def signup(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():

            print(form.cleaned_data)
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)
