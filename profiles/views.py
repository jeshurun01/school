from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import NewUserForm, EditProfileForm
from .models import Profile


def sign_up(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'registration/sign_up.html', context)


@login_required
def edit_profile(request):
    form = EditProfileForm()
    if request.method == 'PUT':
        form = EditProfileForm(request.PUT)
        if form.is_valid():
            form.save()
            return redirect('profiles:profile')

    context = {
        'form': form
    }

    return render(request, 'profiles/edit_profile.html', context)


@login_required
def profile_page(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile
    }
    return render(request, 'profiles/profile.html', context)
