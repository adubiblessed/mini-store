from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import RegisterForm, LoginForm
from .models import User

# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/register_success.html')
        else:
            return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('users:home') 
            else:
                form.add_error(None, 'Invalid username or password.')
    return render(request, 'login.html', {'form': form})

def home(request):
    user = request.user
    if not user.is_authenticated:
        return render(request, 'login.html')
    return render(request, 'users/home.html')