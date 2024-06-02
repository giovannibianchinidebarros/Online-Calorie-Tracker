from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                user = User.objects.create_user(
                    username=username, password=password)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
            except:
                messages.error(request, 'Username already exists')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'authapp/register.html')


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')

    return render(request, 'authapp/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
