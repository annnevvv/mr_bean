"""
URL configuration for mr_bean project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework import routers

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users_app.urls', 'users_app')),
    path('images/', include('image_app.urls', 'images_app')),
    path('api/', include('image_app.urls', 'api_app'))
    # path('api/', include(router.urls), name='api'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT) + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
