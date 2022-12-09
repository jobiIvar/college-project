from django.urls import path
from . import views
app_name = 'facilities'
urlpatterns = [
    path('', views.all, name='all'),
    path('lab/', views.lab, name='lab')
]