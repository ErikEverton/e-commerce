from django.urls import path
from .views.auth_views import SignUpView, LoginView, LogOut

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LoginView.as_view(), name="logout")
]

