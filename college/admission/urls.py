from django.urls import path
from . import views

app_name = 'admission'
urlpatterns = [
    path('ug_admission/', views.admission, name='ug_admission'),
    path('pg_admission/', views.pg_admission, name='pg_admission'),
]
