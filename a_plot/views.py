from django.shortcuts import render

def home_view(request):
    title = "Welcome to Super Camper App"
    context = {
        "title": title,
    }
    return render(request, "index.html", context)