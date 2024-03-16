from django.shortcuts import render
from django.views import View
from users.forms import SignupForm, LoginForm
# Create your views here.

class Register(View):
    def get(self, request):
        form = {'form': SignupForm()}
        return render(request, 'auth/register.html', form)
    
    def post(self, request):
        form = {'form': SignupForm()}



class Login(View):
    def get(self, request):
        form = {'form': LoginForm()}
        return render(request, "auth/login.html", form)

