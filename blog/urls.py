from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path( "",views.blog_list, name="blog_list"),
    path("create/",views.blog_create,name="blog_create"),
    path( "<slug:slug>/",views.blog_detail, name="blog_detail"),
    path("<slug:slug>/update/",views.blog_update,name="blog_update"),
    path( "<slug:slug>/delete/", views.blog_delete, name="blog_delete"),
    path( "category/<slug:slug>/",views.category_posts,name="category_posts"),

]