from django.urls import path
from . import views

app_name = 'administration'
urlpatterns = [
    path('', views.administration, name='administration'),
    path('principal/', views.principal, name="principal"),
    path('correspondent/', views.correspondent, name="correspondent"),
    path('board_members/', views.admin_board, name="board_members")
]
