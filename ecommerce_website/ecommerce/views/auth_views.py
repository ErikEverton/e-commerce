from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from ..forms import SignUpForm, LoginForm


class SignUpView(View):
    def get(self, request):
        data = {'form': SignUpForm()}
        return render(request, 'ecommerce/signup.html', data)
    
    def post(self, request):
        form = SignUpForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if username and password1 and password2 and password1 == password2:
                user = User.objects.create_user(
                    username=username,
                    password=password1
                )

                if user:
                    return HttpResponseRedirect(reverse('login'))

        data = {
            'form': form,
            'error': 'Username or password is invalid'
        }

        return render(request, "ecommerce/signup.html", data)

class LoginView(View):
    def get(self, request):
        data = {'form': LoginForm()}
        return render(request, 'ecommerce/login.html', data)

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            if username and password and authenticate(username=username, password=password):
                login(request)
                return HttpResponseRedirect(reverse('index'))
        
        data = {
            'form': form,
            'error': 'Username or password is invalid'
        }
        return render(request, 'ecommerce/login.html', data)



class LogOut(View):
    def get(self, request):
        pass


