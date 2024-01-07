from django import forms    
from django.forms import ModelForm
from .models import Profile

class ProfileAddForm(ModelForm):
    class Meta:
        model = Profile
        # use the fields from the Profile model
        exclude = ['user']
        
        labels = {
            "realname": "Name",
            "campermode": 'Tent or Camper?',
            "camperstory": "Your Camper Experience",
        }
        widgets = {
            'image': forms.FileInput(),
        }



class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        # choose the fields from the Profile model manually
        fields = ( 'image', 'realname', 'email', 'nationality', 'campermode', 'camperstory', 'fav_campsite')
        
        labels = {
            "realname": "Name",
            "campermode": 'Tent or Camper?',
            "camperstory": "Your Camper Experience",
        }
        widgets = {
            'image': forms.FileInput(),
        }