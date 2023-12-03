from django import forms    
from .models import * 
from django.forms import ModelForm


# Create Plot form
class PlotAddForm(ModelForm):
    class Meta:
        model = Plot
        fields = "__all__"
