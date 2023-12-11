from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html", {})

def experience(request):
    return render(request, "pages/experience.html", {})