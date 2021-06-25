from django.urls import path
from user import views
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    path("login/", views.login, name="login_page"),
    path("logout/", views.logout, name="logout_page"),
    path("signin/", views.Registration.as_view(), name="signin_page"),
    path("", lambda request: redirect(reverse("login_page"))),
]