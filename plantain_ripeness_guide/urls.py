from django.urls import path
from . import views

urlpatterns = [
    path('', views.ripeness_guide, name='ripeness_guide'),
    path('<int:stage_id>/', views.ripeness_detail, name='ripeness_detail'),
    path('add/', views.add_ripeness, name='add_ripeness'),
    path('edit/<int:stage_id>/', views.edit_ripeness, name='edit_ripeness'),
    path('delete/<int:stage_id>/', views.delete_ripeness, name='delete_ripeness'),
]