from django.db import models
import uuid
from django.templatetags.static import static


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

COUNTRIES = (
    ("Spain", "Spain"),
    ("France", "France"),
    ("Portugal", "Portugal"),
    ("Italy", "Italy"),
    ("Germany", "Germany"),
    ("Netherlands", "Netherlands"),
    ("Ireland", "Ireland"),
    ("Belgium", "Belgium"),
    ("Greece", "Greece"),
    ("United Kingdom", "United Kingdom"),
    ("Switzerland", "Switzerland"),
    ("Austria", "Austria"),
    ("Sweden", "Sweden"),
    ("Norway", "Norway"),
    ("Finland", "Finland"),
    ("Denmark", "Denmark"),
    ("Croatia", "Croatia"),
    ("Poland", "Poland"),
    ("Romania", "Romania"),
    ("Bulgaria", "Bulgaria"),
    ("Czech Republic", "Czech Republic"),
    ("Hungary", "Hungary"),
    ("Slovakia", "Slovakia"),
    ("Slovenia", "Slovenia"),
    ("Luxembourg", "Luxembourg"),
    ("Latvia", "Latvia"),
    ("Estonia", "Estonia"),
    ("Lithuania", "Lithuania"),
    ("Malta", "Malta"),
    ("Cyprus", "Cyprus"),
    ("Iceland", "Iceland"),
    ("Liechtenstein", "Liechtenstein"),
    ("Monaco", "Monaco"),
    ("San Marino", "San Marino"),
    ("Andorra", "Andorra"),
    ("Albania", "Albania"),
    ("Armenia", "Armenia"),
    ("Azerbaijan", "Azerbaijan"),
    ("Belarus", "Belarus"),
    ("Bosnia and Herzegovina", "Bosnia and Herzegovina"),
    ("Georgia", "Georgia"),
    ("Kazakhstan", "Kazakhstan"),
    ("Kosovo", "Kosovo"),
    ("Macedonia", "Macedonia"),
    ("Moldova", "Moldova"),
    ("Montenegro", "Montenegro"),
    ("Russia", "Russia"),
    ("Serbia", "Serbia"),
    ("Turkey", "Turkey"),
    ("Ukraine", "Ukraine"),
)

SEASONS = (
    ("Low", "Low"),
    ("Mid", "Mid"),
    ("High", "High"),  
)





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




class Plot(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    season = models.CharField(max_length=100, choices=SEASONS, default="Mid", blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    plot = models.CharField(max_length=100)
    categories = models.CharField(max_length=25, choices=CATEGORIES, default=1)
    what3words = models.URLField(blank=True, null=True)
    campsite = models.CharField(max_length=100, blank=True, null=True)
    countries = models.CharField(max_length=100, choices=COUNTRIES, default="Spain")
    list_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name="plots")
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-list_date"]






class Comment(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name="comments")
    parent_plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="comments")
    body = models.CharField(max_length=600)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:20]}... '
        except:
            return f'no author : {self.body[:20]}... '
        
    class Meta:
        ordering = ["-created"]