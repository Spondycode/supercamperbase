from django.contrib import admin
from .models import *

admin.site.register(Plot)
admin.site.register(Comment)
# admin.site.register(Tag) safe let's go comment pan