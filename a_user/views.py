from django.shortcuts import render
from django.contrib.auth import logout
from a_plot.views import *
from a_user.views import *
from a_user.forms import *

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout



def profile_view(request):
    if request.user.is_authenticated:
        plots = Plot.objects.filter(owner=request.user)  # Fetch plots created by the logged in user
        profile = request.user.profile  
        context = {
            "plots": plots,
            "profile": profile,
        }
        return render(request, "a_user/profile.html", context)
        
    else:
        messages.success(request, "You need to login first")
        return redirect("/login")
    
    
def profile_edit_view(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        form = ProfileAddForm(instance=profile)
        context = {
            "form": form,
            "profile": profile,
        }
        if request.method == "POST":
            form = ProfileAddForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully")
                return redirect("profile")
        return render(request, "a_user/profile_edit.html", context)
        
    else:
        messages.success(request, "You need to login first")
        return redirect("/login")