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
    # nationality = forms.CharField(max_length=100, required=True)
    # test = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2"]
        
        
class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body": forms.TextInput(attrs={'placeholder': 'Add a comment...'}),
        }
        labels = {
            "body": "",
        }
        
        
        
class ReplyCreateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ["body"]
        widgets = {
            "body": forms.TextInput(attrs={'placeholder': 'Add a reply...'}),
        }
        labels = {
            "body": "",
        }