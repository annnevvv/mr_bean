from django.urls import path, include
from django.conf.urls.static import static

from image_app.views import ImageModelViewSet, ImageCommenModelViewSet
from mr_bean import settings
from users_app.views import UserAccountTierViewSet, UserProfileModelViewSet

from rest_framework import routers
from rest_framework.routers import DefaultRouter


app_name = 'api_app'

router = routers.DefaultRouter()

# users_app

router.register('user_account_tiers', UserAccountTierViewSet)
router.register('user_profiles', UserProfileModelViewSet)

# image_app

router.register('image_models', ImageModelViewSet)
router.register('image_comment_models', ImageCommenModelViewSet)


urlpatterns = [
    path('', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
