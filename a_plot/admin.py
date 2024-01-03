from django.contrib import admin
from .models import *

admin.site.register(Plot)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(LikedPlot)
admin.site.register(LikedComment)