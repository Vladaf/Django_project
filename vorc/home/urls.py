from django.urls import path
from home import views
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    path("home/", views.home, name="home_page"),
    path("about/", views.about, name="about_us_page"),
    path("contacts/", views.contacts, name="contacts_page"),
    path("", lambda request:redirect (reverse("home_page"))),
]