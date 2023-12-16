from django.db import models
from django.contrib.auth.models import User
   


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/" , null=True, blank=True)
    realname = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)
    campermode = models.CharField(max_length=20, null=True, blank=True)
    camperstory = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
    
