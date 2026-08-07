from django.urls import path
from . import views


app_name = "education"

urlpatterns = [

    path(  "", views.education_list, name="education_list"),
    path( "<int:pk>/", views.education_detail, name="education_detail"),
    
    
]