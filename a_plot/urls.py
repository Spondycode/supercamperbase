from django.urls import path
from .views import plot_view, add_plot_view, delete_plot_view, edit_plot_view, my_plots_view, like_plot, like_comment, search_plots_view, search_categories_view, campsite_plots_view, wild_plots_view, official_plots_view, search_countries_view, country_view, comment_sent, delete_comment, reply_sent, delete_reply, questions_view

urlpatterns = [
    path("show_plot/<plot_id>/", plot_view, name="show_plot"),
    path("add_plot/", add_plot_view, name="add_plot"),
    path("delete_plot/<pk>/", delete_plot_view, name="delete_plot"),
    path("edit_plot/<pk>/", edit_plot_view, name="edit_plot"),
    path("my_plots/", my_plots_view, name="my_plots"),
    path("myplots/", my_plots_view, name="my_plots"),
    path("plot/like/<pk>/", like_plot, name="like_plot"),
    path("comment/like/<pk>/", like_comment, name="like_comment"),
    path("search_plots/", search_plots_view, name="search_plots"),
    path("search_categories/", search_categories_view, name="search_categories"),
    path("campsite_plots/", campsite_plots_view, name="campsite-plots"),
    path("wild_plots/", wild_plots_view, name="wild-plots"),
    path("official_plots/", official_plots_view, name="official-plots"),
    path("search_countries/", search_countries_view, name="search_countries"),
    path("country/<plot_country>/", country_view, name="country"),
    path("commentsent/<pk>/", comment_sent, name="comment_sent"),
    path("delete_comment/<pk>/", delete_comment, name="delete_comment"),
    path("replysent/<pk>/", reply_sent, name="reply_sent"),
    path("delete_reply/<pk>/", delete_reply, name="delete_reply"),
    path("questions/", questions_view, name="questions"),
    
]