"""
URL configuration for A_CORE project.
"""
from django.contrib import admin
from django.urls import path, include
from a_plot.views import *
from a_user.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("a_user.urls")),
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
]
