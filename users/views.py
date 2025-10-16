from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, template_name='user/register.html',
                    context={'form':form})


def auth_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid:
            user = form.get_user()
            login(request, user)
            return redirect('users:user_list')
    else:
        form = AuthenticationForm()
    return render(request, template_name='users/login.html', 
                  context={'form':form})


def auth_logout_view(request):
    logout(request)
    return('users:login')


def user_list_view(request):
    if request.method == 'GET':
        users = User.objects.all().order_by('-id')
    return render(request, template_name='users/user_list.html', context={'users':users})