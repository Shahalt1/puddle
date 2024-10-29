from django.contrib.auth import views as views_auth
from django.urls import path
from . import views
from .forms import LoginForm

app_name = "core"
urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("signup/", views.signup, name="signup"),
    path(
        "login/",
        views_auth.LoginView.as_view(
            template_name="core/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
]
