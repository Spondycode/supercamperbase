from django.db import models
import uuid
from django.templatetags.static import static

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    # take care od the plural form of the model name
    class Meta:
        verbose_name_plural = "Countries"
        

class Tag(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to="icons/", blank=True, null=True)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Tags"        
           
           
CATEGORIES = (
    ("Campsite", "Campsite"),
    ("Official", "Official"),
    ("Wild", "Wild"),
)

CATEGORIES_PARAMS = {
    1: {"slug": "campsite", "name": "Campsite"},
    2: {"slug": "official", "name": "Official"},
    3: {"slug": "wild", "name": "Wild"},
}


class Plot(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    plot = models.CharField(max_length=100)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="plots", blank=True, null=True)
    categories = models.CharField(max_length=25, choices=CATEGORIES, default=1)
    what3words = models.URLField(blank=True, null=True)
    campsite = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="plots", blank=True, null=True)
    list_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name="plots")
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-list_date"]
    
    @property
    def plotty(self):
        try:
            plotty = self.image.url
        except:
            plotty = static('images/default.jpg')
        return plotty
