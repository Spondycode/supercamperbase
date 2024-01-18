from django import forms    
from .models import * 
from django.forms import ModelForm
from .models import *

class ProfileAddForm(ModelForm):
    class Meta:
        model = Profile
        # use the fields from the Profile model
        exclude = ['user', 'level', 'plot_reports', 'numplots']
        
        labels = {
            "realname": "Name",
            "campermode": 'Tent or Camper?',
            "camperstory": "Your Camper Experience",
        }
        widgets = {
            'image': forms.FileInput(),
        }