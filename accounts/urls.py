from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    # accounts/hello/
    path("hello/", views.hello),
    # accounts/signup/
    path("signup/", views.signup, name="signup"),
    # accounts/logout/
    path("logout/", LogoutView.as_view(), name="logout"),
    # accounts/login/
    path(
        "login/", LoginView.as_view(template_name="accounts/login.html"), name="login"
    ),
]
