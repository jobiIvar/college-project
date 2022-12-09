from django.urls import path
from . import views
app_name = 'academics'

urlpatterns = [
    path('', views.academics, name='academics'),
    path('course/', views.course, name="course")
]