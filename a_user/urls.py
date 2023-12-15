from django.urls import path
from .views import *
from django.conf import settings #add this
from django.conf.urls.static import static #add this

urlpatterns = [
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", profile_edit_view, name="profile-edit"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)