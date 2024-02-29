from django.urls import path
from .views.ecommerce_views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index")
]

