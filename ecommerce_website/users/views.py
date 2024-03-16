from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from users.forms import SignupForm, LoginForm
# Create your views here.

class Register(View):
    def get(self, request):
        data = {'form': SignupForm()}
        return render(request, 'auth/register.html', data)
    
    def post(self, request):
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            data = {'form': form, 'error': 'username, email ou password é inválido'}
            return render(request, 'auth/register.html', data)



class Login(View):
    def get(self, request):
        data = {'form': LoginForm()}
        return render(request, "auth/login.html", data)
    
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
            data = {'form': form, 'error': 'username, email ou password é inválido'}
            return render(request, 'auth/login.html', data)
