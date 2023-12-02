from django.shortcuts import render
from .models import *
from django.forms import ModelForm  # for add_plot_view

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

def plot_view(request, plot_id):
    plot = Plot.objects.get(id=plot_id)
    context = {
        "plot": plot,
    }
    return render(request, "plotpage.html", context)


class PlotAddForm(ModelForm):
    class Meta:
        model = Plot
        fields = ["title", "description", "price", "image", "plot", "what3words", "campsite", "country"]


def add_plot_view(request):
    form = PlotAddForm()
    title = "Add a plot"
    context = {
        "title": title,
        "form": form,
    }
    return render(request, "add_plot.html", context)

