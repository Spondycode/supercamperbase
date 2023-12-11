from django.urls import path
from .views import *

urlpatterns = [
    path("show_plot/<plot_id>/", plot_view, name="show_plot"),
    path("add_plot/", add_plot_view, name="add_plot"),
    path("delete_plot/<pk>/", delete_plot_view, name="delete_plot"),
    path("edit_plot/<pk>/", edit_plot_view, name="edit_plot"),
    path("my_plots/", my_plots_view, name="my_plots"),
    path("profile/", profile_view, name="profile"),
    path("myplots/", my_plots_view, name="my_plots"),
]