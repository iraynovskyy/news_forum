from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user_signup/", views.user_signup, name="user_signup"),
    path("user_login/", views.user_login, name="user_login"),
    path("post_creation/", views.post_creation, name="post_creation"),
    path("post_update/<int:post_id>/", views.post_update, name="post_creation"),
    path("post_delete/<int:post_id>/", views.post_delete, name="post_delete"),
    path("post=<post_id>/like", views.post_like, name="post_like"),
]
