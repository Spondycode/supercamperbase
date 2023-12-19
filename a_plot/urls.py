from django.urls import path
from .views import *

urlpatterns = [
    path("show_plot/<plot_id>/", plot_view, name="show_plot"),
    path("add_plot/", add_plot_view, name="add_plot"),
    path("delete_plot/<pk>/", delete_plot_view, name="delete_plot"),
    path("edit_plot/<pk>/", edit_plot_view, name="edit_plot"),
    path("my_plots/", my_plots_view, name="my_plots"),
    path("myplots/", my_plots_view, name="my_plots"),
    path("search_plots/", search_plots_view, name="search_plots"),
    path("search_categories/", search_categories_view, name="search_categories"),
    path("search_countries/", search_countries_view, name="search_countries"),
    path("country/<plot_country>/", country_view, name="country"),
]