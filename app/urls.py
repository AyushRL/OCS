from django.urls import path
from .views import home, validate

urlpatterns = [
    path("home", home, name  = "home"),
    path("login", validate, name = "login"),
    path("", home),
]
