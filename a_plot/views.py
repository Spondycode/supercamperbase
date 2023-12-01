from django.shortcuts import render
from .models import *

def home_view(request):
    title = "Welcome to Super Camper App"
    plots = Plot.objects.all()
    context = {
        "title": title,
        "plots": plots,
    }
    return render(request, "index.html", context)

def about_view(request):
    title = "About Super Camper App"
    context = {
        "title": title,
    }
    return render(request, "about.html", context)

