from django.urls import path
from .views.auth_views import SignUpView, LoginView, LogOut
from .views.ecommerce_views import IndexView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogOut.as_view(), name="logout"),
]

urlpatterns += [
    path("", IndexView.as_view(), name="index")
]

