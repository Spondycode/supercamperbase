from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import *
from django.forms import ModelForm
from django import forms # for add_plot_view
from .forms import *
from django.contrib import messages 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# def home_view(request, tag=None):
#     if tag:
#         plots = Plot.objects.filter(tags__slug=tag)
#     else:
#         plots = Plot.objects.all()
#     context = {
#         "plots": plots,
#     }
#     return render(request, "index.html", context)

# HOME PAGE
def home_view(request):
    plots = Plot.objects.all()
    context = {
        "plots": plots,
    }
    return render(request, "index.html", context)


# Filter by country
def country_view(request):
    plots = Plot.objects.filter(country=request.country.name)
    context = {
        "plots": plots,
    }
    return render(request, "a_plots/country_view.html", context)





def about_view(request):
    title = "About Super Camper App"
    context = {
        "title": title,
    }
    return render(request, "about.html", context)



def questions_view(request):
    title = "Frequently Asked Questions"
    context = {
        "title": title,
    }
    return render(request, "a_plots/questions.html", context)





def plot_view(request, plot_id):
    plot = Plot.objects.get(id=plot_id)
    commentform = CommentCreateForm()
    replyform = ReplyCreateForm()
    context = {
        "plot": plot,
        "commentform": commentform,
        "replyform": replyform,
    }
    return render(request, "a_plots/plotpage.html", context)



# Comment sent function
@login_required
def comment_sent(request, pk):
    plot = get_object_or_404(Plot, id=pk)
    
    if request.method == "POST":
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user # get the logged in user
            comment.parent_plot = plot
            comment.save()
        
    return redirect("show_plot", plot_id=pk)



@login_required
def reply_sent(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    
    if request.method == "POST":
        form = ReplyCreateForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user # get the logged in user
            reply.parent_comment = comment
            reply.save()
        
    return redirect("show_plot", comment.parent_plot.id)



@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk, author=request.user)
    context = {
        "comment": comment,
    }
    
    if request.method == "POST":
        comment.delete()
        messages.success(request, "Comment deleted successfully")
        return redirect("show_plot", comment.parent_plot.id)
    
    return render(request, "a_plots/delete_comment.html", context)



@login_required
def delete_reply(request, pk):
    reply = get_object_or_404(Reply, id=pk, author=request.user)
    context = {
        "reply": reply,
    }
    
    if request.method == "POST":
        reply.delete()
        messages.success(request, "Reply deleted successfully")
        return redirect("show_plot", reply.parent_comment.parent_plot.id)
    
    return render(request, "a_plots/delete_reply.html", context)




# Add a plot
@login_required
def add_plot_view(request):
    submitted = False
    if request.method == "POST":
        form = PlotAddForm(request.POST, request.FILES)
        if form.is_valid():
            plot = form.save(commit=False)
            plot.owner = request.user # get the logged in user
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


# To edit a plot, we need to get the plot id from the URL, then get the plot from the database, and then edit it.
@login_required
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
            plot = form.save(commit=False)
            plot.user = request.user # get the logged in user
            form.save()
            messages.success(request, "Plot updated successfully")
            return redirect("profile")
    return render(request, "a_plots/edit_plot.html", context)


# To delete the plot, we need to get the plot id from the URL, then get the plot from the database, and then delete it.
@login_required
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


# search plots by category
def search_categories_view(request):
    if request.method == "POST":
        search = request.POST["search"]
        plots = Plot.objects.filter(categories__contains=search)
        context = {
            "plots": plots,
            "search": search
        }
        return render(request, "a_plots/category_search.html", context)
        plots = Plot.objects.filter(categories__icontains=query)
    else:
        plots = Plot.objects.all()
    context = {
        "plots": plots,
    }
    
    return render(request, "a_plots/category_search.html", context)


def campsite_plots_view(request):
    if request.user.is_authenticated:
        plots = Plot.objects.filter(categories__icontains="Campsite")  # Fetch plots with category "Campsite"
        context = {
            "plots": plots,
        }
        return render(request, "a_plots/campsite_plots.html", context)
        
    else:
        messages.success(request, "You need to login first")
        return redirect("/login")



def official_plots_view(request):
    if request.user.is_authenticated:
        plots = Plot.objects.filter(categories__icontains="Official")  # Fetch plots with category "Official"
        context = {
            "plots": plots,
        }
        return render(request, "a_plots/official_plots.html", context)
        
    else:
        messages.success(request, "You need to login first")
        return redirect("/login")



def wild_plots_view(request):
    if request.user.is_authenticated:
        plots = Plot.objects.filter(categories__icontains="Wild")  # Fetch plots with category "Wild"
        context = {
            "plots": plots,
        }
        return render(request, "a_plots/wild_plots.html", context)
        
    else:
        messages.success(request, "You need to login first")
        return redirect("/login")






# search plots by country
def search_countries_view(request):
    if request.method == "POST":
        search = request.POST["search"]
        plots = Plot.objects.filter(countries__contains=search)
        context = {
            "plots": plots,
            "search": search
        }
        return render(request, "a_plots/country_search.html", context)
        plots = Plot.objects.filter(countries__icontains=query)
    else:
        plots = Plot.objects.all()
    context = {
        "plots": plots,
    }
    
    return render(request, "a_plots/country_search.html", context)


def like_plot(request, pk):
    plot = get_object_or_404(Plot, id=pk)
    user_exists = plot.likes.filter(username=request.user.username).exists()
   
    if plot.owner != request.user:
        if user_exists:
            plot.likes.remove(request.user)
        else:
            plot.likes.add(request.user)
        
    return render(request, "a_plots/plotpage.html", {"plot": plot})


def like_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    user_exists = comment.likes.filter(username=request.user.username).exists()
   
    if comment.author != request.user:
        if user_exists:
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)
        
    return HttpResponse(comment.likes.count() )


