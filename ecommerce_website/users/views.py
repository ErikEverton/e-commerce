from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreationForm, LoginForm, UserUpdateForm, ProfileUpdateForm


class Register(View):
    def get(self, request):
        data = {'form': UserCreationForm()}
        return render(request, 'ecommerce/auth/signup.html', data)
    
    def post(self, request):
        form = UserCreationForm(data=request.POST)

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

        return render(request, "ecommerce/auth/signup.html", data)

class LoginView(View):
    def get(self, request):
        data = {'form': LoginForm()}
        return render(request, 'ecommerce/auth/login.html', data)

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if username and password and user:
                login(request, user=user)
                return HttpResponseRedirect(reverse('index'))
        
        data = {
            'form': form,
            'error': 'Username or password is invalid'
        }
        return render(request, 'ecommerce/auth/login.html', data)



class LogOut(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))
    

class Profile(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            "user_form": UserUpdateForm(instance=request.user),
            "profile_form": ProfileUpdateForm(instance=request.user.profile),
        }
        return render(request, 'ecommerce/profile/profile.html', context)
    
    def post(self, request):
        form = ProfileUpdateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
        
