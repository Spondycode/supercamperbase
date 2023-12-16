"""
URL configuration for A_CORE project.
"""
from django.contrib import admin
from django.urls import path, include
from a_plot.views import *
from a_user.views import *
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("home/", home_view, name="home"),
    path("", include("a_user.urls")),
    path("", home_view, name="home"),
    # path("category/<tag>", home_view, name="category"),
    path("about/", about_view, name="about"),
    path("", include("a_plot.urls")),
    path("", include('django.contrib.auth.urls')),
    path("register/", register_view, name="register"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

