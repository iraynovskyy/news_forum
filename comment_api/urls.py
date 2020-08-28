from django.urls import path
from . import views

urlpatterns = [
    path('all', views.comments_all, name="comments_all"),
    path('comment_creation/', views.comment_creation, name="comment_creation"),
    path(
        'comment_update/<int:comment_id>/', views.comment_update,
        name="comment_update"
    ),
    path(
        'comment_delete/<int:comment_id>/', views.comment_delete,
        name="comment_delete"
    ),
]
