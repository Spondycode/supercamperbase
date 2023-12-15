from django.urls import path
from .views import *

urlpatterns = [
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", profile_edit_view, name="profile-edit"),
]

