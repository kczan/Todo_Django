from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCreateForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import password_validation
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_user(request):

    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        else:
            print(user_form.errors)
    else:
        user_form = UserCreateForm()
    context = {
        'user_form': user_form,
        'page_title': 'Register new user',
        'password1_help': password_validation.password_validators_help_text_html(),
    }
    return render(request, 'users/register.html', context)


@login_required
def user_profile(request):
    user = request.user
    username = user.username

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            messages.success(request, f'{username} data updated!')
            return redirect('profile')
        else:
            print(user_form.errors)
            print(prof_form.errors)
    else:
        user_form = UserUpdateForm(instance=request.user)
        prof_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'page_title': username.capitalize() + ' profile',
        'user': user,
        'user_form': user_form,
        'prof_form': prof_form,
    }
    return render(request, 'users/profile.html', context)


