from django.urls import path
from . import views


app_name = "experience"


urlpatterns = [
    path(
        "",
        views.experience_list,
        name="experience_list"
    ),

    path(
        "create/",
        views.experience_create,
        name="experience_create"
    ),
]