from django.urls import path
import ecommerce.views as views

app_name = "ecommerce"
urlpatterns = [
    path('home/', views.IndexView.as_view(), name="home"),
]

