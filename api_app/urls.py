from django.urls import path, include

from image_app.views import ImageModelViewSet, ImageCommenModelViewSet
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
