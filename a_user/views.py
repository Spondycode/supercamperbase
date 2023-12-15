from django.shortcuts import render
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout

def profile_view(request):
    return render(request, 'a_user/profile.html')