from django import forms    
from .models import * 
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


# Create Plot form
class PlotAddForm(ModelForm):
    class Meta:
        model = Plot
        fields = ['title', 'description', 'price', 'season', 'image', 'plot', 'what3words', 'campsite', 'countries', 'categories', 'owner']
        


class PlotEditForm(ModelForm):
    class Meta:
        model = Plot
        fields = ["title", "description", "price", 'season', "image", "plot", "what3words", "campsite", "countries", "categories"]
        
        
        
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nationality = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = User 
        fields = ["username", "nationality", "email", "password1", "password2"]