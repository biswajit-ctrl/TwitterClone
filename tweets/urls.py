from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("upload/", views.upload, name="upload"),
    path("<id>/delete/", views.delete_view, name="delete"),
    path("<id>/edit/", views.edit, name="edit"),
    path("<id>/like/", views.like_function, name="like"),
    path("<id>/dislike/", views.dislike_function, name="dislike"),

]
