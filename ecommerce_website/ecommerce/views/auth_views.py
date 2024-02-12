from django.shortcuts import render
from django.views import View
from ..forms import SignUpForm


class SignUpView(View):
    def get(self, request):
        data = {'form': SignUpForm()}
        return render(request, 'ecommerce/signup.html', data)


class LoginView(View):
    def get(self, request):
        pass


class LogOut(View):
    def get(self, request):
        pass


