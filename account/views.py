from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('app-school:home')
            else:
                return HttpResponse('Somethings Wrong!!')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password'] == cd['confirmpassword']:
                user = User.objects.create_user(
                    username=cd['username'],
                    email=cd['email'],
                    password=cd['password']
                    )
                return redirect('app-account:login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})