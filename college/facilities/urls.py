from django.urls import path
from . import views
app_name = 'facilities'
urlpatterns = [
    path('', views.all, name='all'),
    path('lab/', views.lab, name='lab'),
    path('library/', views.library, name='library'),
    path('sport/', views.sport, name='sport'),
    path('smart_class/', views.smart_class, name="smart_class"),
]
