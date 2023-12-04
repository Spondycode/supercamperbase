from django import forms    
from .models import * 
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


# Create Plot form
class PlotAddForm(ModelForm):
    class Meta:
        model = Plot
        fields = "__all__"


class PlotEditForm(ModelForm):
    class Meta:
        model = Plot
        fields = "__all__"
        exclude = ["user"]
        
        
        
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nationality = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = User 
        fields = ["username", "nationality", "email", "password1", "password2"]