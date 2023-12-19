from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from django.forms import ModelForm
from django import forms # for add_plot_view
from .forms import *
from django.contrib import messages 
from django.contrib.auth import login, logout, authenticate 

# def home_view(request, tag=None):
#     if tag:
#         plots = Plot.objects.filter(tags__slug=tag)
#     else:
#         plots = Plot.objects.all()
#     context = {
#         "plots": plots,
#     }
#     return render(request, "index.html", context)

def home_view(request):
    plots = Plot.objects.all()
    context = {
        "plots": plots,
    }
    return render(request, "index.html", context)


def category_view(request, tag):
      # Corrected here
    context = {
        "plots": plots,
    }
    return render(request, "category.html", context)


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
    return render(request, "a_plots/plotpage.html", context)


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
    return render(request, "a_plots/add_plot.html", context)

# To delete the post, we need to get the post id from the URL, then get the post from the database, and then delete it.
def delete_plot_view(request, pk):
    plot = Plot.objects.get(id=pk)
    context = {
        "plot": plot,
    }
    
    if request.method == "POST":
        plot.delete()
        messages.success(request, "Plot deleted successfully")
        return redirect("home")
    return render(request, "a_plots/delete_plot.html", context)


# To edit a plot, we need to get the plot id from the URL, then get the plot from the database, and then edit it.
def edit_plot_view(request, pk):
    plot = Plot.objects.get(id=pk)
    form = PlotAddForm(instance=plot)
    context = {
        "form": form,
        "plot": plot,
    }
    if request.method == "POST":
        form = PlotEditForm(request.POST, instance=plot)
        if form.is_valid():
            form.save()
            messages.success(request, "Plot updated successfully")
            return redirect("home")
    return render(request, "a_plots/edit_plot.html", context)


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully")
            return redirect("/home")
    else:
        form = RegisterForm()
        
    return render(request, "registration/register.html", {"form": form})


    
    
def my_plots_view(request):
    if request.user.is_authenticated:
        plots = Plot.objects.filter(user=request.owner)  # Fetch plots created by the logged in user
        context = {
            "plots": plots,
        }
        return render(request, "a_plots/myplots.html", context)
        
    else:
        messages.success(request, "You need to login first")
        return redirect("/login")


# SEarch plots
def search_plots_view(request):
    
    if request.method == "POST":
        search = request.POST["search"]
        plots = Plot.objects.filter(title__contains=search)
        context = {
            "plots": plots,
            "search": search
        }
        return render(request, "a_plots/plot_search.html", context)
        plots = Plot.objects.filter(title__icontains=query)
        
    else:
        plots = Plot.objects.all()
    context = {
        "plots": plots,
    }
    return render(request, "a_plots/plot_search.html", context)


CATEGORIES = (
    (1, "Campsite"),
    (2, "Official"),
    (3, "Wild"),
)