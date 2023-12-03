from django.db import models
import uuid

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    # take care od the plural form of the model name
    class Meta:
        verbose_name_plural = "Countries"


class Plot(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    plot = models.CharField(max_length=100)
    what3words = models.URLField(blank=True, null=True)
    campsite = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="plots", blank=True, null=True)
    list_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="plots")
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-list_date"]
    
