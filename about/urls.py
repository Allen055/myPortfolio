from django.urls import path
from . import views

app_name = "about"

urlpatterns = [
    path("", views.about, name="about"),
    path("story/", views.story, name="story"),
    path("mission/", views.mission, name="mission"),
]