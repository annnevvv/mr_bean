from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from mr_bean import settings

from .views import SignupView, UserDasboard, UserProfileDetailView

app_name = 'users_app'

urlpatterns = [

    # autentication

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),

    #  user side

    path('dashboard/', UserDasboard.as_view(), name='dashboard'),
    path('user_profile/',
         UserProfileDetailView.as_view(), name='user_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
