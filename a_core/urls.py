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
    path("category/<tag>", home_view, name="category"),
    path("home/", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("", include("a_plot.urls")),
    path("", include('django.contrib.auth.urls')),
    path("register/", register_view, name="register"),
]
