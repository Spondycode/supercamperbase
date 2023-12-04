"""
URL configuration for A_CORE project.
"""
from django.contrib import admin
from django.urls import path, include
from a_plot.views import *
from a_user.views import *
from a_plot import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("a_user.urls")),
    path("", home_view, name="home"),
    path("home/", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("show_plot/<plot_id>/", plot_view, name="show_plot"),
    path("add_plot/", add_plot_view, name="add_plot"),
    path("delete_plot/<pk>/", delete_plot_view, name="delete_plot"),
    path("edit_plot/<pk>/", edit_plot_view, name="edit_plot"),
    path("", include('django.contrib.auth.urls')),
    path("register/", register_view, name="register"),
]
