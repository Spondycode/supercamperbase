from django.db import models
from django.contrib.auth.models import User


MODES = (
    ("Hammock", "Hammock"),
    ("Small Tent", "Small Tent"),
    ("Large Tent", "Large tent"),
    ("Car", "Car"),
    ("Van", "Van"),
    ("CamperVan", "CamperVan"),
    ("Motorhome", "Motorhome"),
    ("Small Caravan", "Small Caravan"),
    ("Large Caravan", "Large Caravan"),
    ("Trailer Tent", "Trailer Tent"),
    ("Cabin/Mobile Home", "Cabin/Mobile Home"),
    ("Under the Stars", "Under the Stars"),
)

LEVELS = (
    ("SC_Founder1", "SuperCamper Founder1"),
    ("SC_Founder2", "SuperCamper Founder2"),
    ("New_SuperCamper", "New SuperCamper"),
    ("SuperCamper", "SuperCamper"),
    ("SuperCamper Expert", "SuperCamper Expert"),
    ("SuperCamper Master", "SuperCamper Master"),
    ("Restricted SuperCamper", "Restricted SuperCamper"),
    ("Banned", "Banned"),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/" , null=True, blank=True)
    realname = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)
    campermode = models.CharField(max_length=20, choices=MODES, default="Hammock", null=True, blank=True)
    camperstory = models.TextField(null=True, blank=True)
    fav_campsite = models.CharField(max_length=20, null=True, blank=True)
    level = models.CharField(max_length=30, choices=LEVELS, default="New SuperCamper", null=True, blank=True)
    plot_reports = models.IntegerField(default=0, null=True, blank=True)
    numplots = models.IntegerField(default=0, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
    
