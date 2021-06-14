from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "user_login"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
]