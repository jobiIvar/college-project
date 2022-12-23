"""college URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from credentials import views

# Serializers define the API representation.


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('myapi', include(router.urls)),
    path('credentials/', include('credentials.urls')),
    path('contact/', include('contact.urls')),
    path('facilities/', include('facilities.urls')),
    path('admission/', include('admission.urls')),
    path('academics/', include('academics.urls')),
    path('administration/', include('administration.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
