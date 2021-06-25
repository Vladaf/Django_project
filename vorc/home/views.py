from django.shortcuts import render

def home(request):
    context = {"name_page": "home"}
    return render(request, "home.html", context)

def about(request):
    context = {"name_page": "about us"}
    return render(request, "about.html", context)

def contacts(request):
    context = {"name_page": "contacts"}
    return render(request, "contacts.html", context)