from django.contrib import admin
from django.urls import path, include
from crud_api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.welcome, name="welcome"),
    path("news/", include("crud_api.urls")),
    path("news/comment/", include("comment_api.urls")),
]
