from django import forms    
from .models import * 
from django.forms import ModelForm
from .models import Profile

class ProfileAddForm(ModelForm):
    class Meta:
        model = Profile
        # use the fields from the Profile model
        fields = ['user', 'image', 'realname', 'email', 'nationality', 'campermode', 'camperstory']
        labels = {
            "campermode": 'Tent or Camper?',
        }