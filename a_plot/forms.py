from django import forms    
from .models import Plot, Comment, Reply
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


# Create Plot form
class PlotAddForm(ModelForm):
    class Meta:
        model = Plot
        fields = ['title', 'description', 'price', 'season', 'image', 'plot', 'what3words', 'campsite', 'countries', 'categories']
        labels = {
            "title": "Title",
            "description": "Description",
            "price": "Price",
            "season": "Season - To give the price some extra context",
            "image": "Picture of the plot",
            "plot": "Plot",
            "what3words": "What3words - to find it on the map",
            "campsite": "Campsite",
            "countries": "Countries",
            "categories": "What sort of Camping spot is it?",
        }
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '** What do you want to call it?'}),
            'plot': forms.TextInput(attrs={'placeholder': '** Enter the plot number or None'}),
            'what3words': forms.TextInput(attrs={'placeholder': '** Really need this for non campsite situations'}),
            'campsite': forms.TextInput(attrs={'placeholder': '** Enter the campsite name or None'}),
        }

class PlotEditForm(ModelForm):
    class Meta:
        model = Plot
        fields = ["title", "description", "price", 'season', "image", "plot", "what3words", "campsite", "countries", "categories"]
        
        
        
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
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