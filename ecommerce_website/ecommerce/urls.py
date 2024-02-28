from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.auth_views import SignUpView, LoginView, LogOut
from .views.ecommerce_views import IndexView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogOut.as_view(), name="logout"),
]

urlpatterns += [
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]

urlpatterns += [
    path("", IndexView.as_view(), name="index")
]

