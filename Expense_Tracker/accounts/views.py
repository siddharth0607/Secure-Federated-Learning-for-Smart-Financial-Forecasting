from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm  # You import these forms
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)  # But use CustomUserCreationForm here
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to dashboard after login
    else:
        form = RegisterForm()  # Same issue here
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)  # But use CustomAuthenticationForm here
        if form.is_valid():
            user = form.get_user()  # Make sure LoginForm has get_user method
            login(request, user)
            return redirect('home')  
    else:
        form = LoginForm()  # Same issue here
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)  
    return redirect('login')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after signup
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})