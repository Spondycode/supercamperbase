from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from django.forms import ModelForm
from django import forms # for add_plot_view
from .forms import PlotAddForm # for add_plot_view

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


def add_plot_view(request):
    submitted = False
    if request.method == "POST":
        form = PlotAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/?submitted=True")
        else:
            print(form.errors)
    else:
        form = PlotAddForm()  # Create an instance of PlotAddForm
        if "submitted" in request.GET:
            submitted = True
    context = {
        "form": form,
        "submitted": submitted,
    }
    print(form.errors)
    return render(request, "add_plot.html", context)

# To delete the post, we need to get the post id from the URL, then get the post from the database, and then delete it.
def delete_plot_view(request, pk):
    plot = Plot.objects.get(id=pk)
    context = {
        "plot": plot,
    }
    
    if request.method == "POST":
        plot.delete()
        return redirect("home")
    return render(request, "delete_plot.html", context)
