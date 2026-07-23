from django.urls import path
from . import views


app_name = "education"

urlpatterns = [

    path(  "", views.education_list, name="education_list"),

    path(  "create/", views.education_create, name="education_create"),

    path( "<int:pk>/", views.education_detail, name="education_detail"),

    path("<int:pk>/update/",views.education_update, name="education_update" ),

    path("<int:pk>/delete/",views.education_delete,name="education_delete" ),
]