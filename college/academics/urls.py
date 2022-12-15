from django.urls import path
from . import views
app_name = 'academics'

urlpatterns = [
    path('', views.academics, name='academics'),
    path('course/', views.course, name="course"),
    path('rank_holders/', views.rank_holder, name="rank_holders"),
    path('university_player', views.university_player, name="university_player")
]