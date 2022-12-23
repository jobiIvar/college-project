from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views
app_name = 'credentials'
urlpatterns = [
    # path("api/", csrf_exempt(views.APIView.as_view())),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout')
]
