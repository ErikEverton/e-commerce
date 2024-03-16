from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from users.forms import SignupForm, LoginForm
# Create your views here.

class Register(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'auth/register.html', {'form': form})
    
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'auth/register.html', {'form': form})



class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "auth/login.html", {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, email=email, password=password)
            if user:
                login(request, user)
                return redirect('ecommerce:home')
        else:
            return render(request, 'auth/login.html', {'form': form})
