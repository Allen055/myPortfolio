from django.urls import path
from . import views

app_name = "portfolio"
urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('create/', views.portfolio_create, name='portfolio_create'),
    path('<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
    path('<int:pk>/update/', views.portfolio_update, name='portfolio_update'),
    path('<int:pk>/delete/', views.portfolio_delete, name='portfolio_delete'),
]
