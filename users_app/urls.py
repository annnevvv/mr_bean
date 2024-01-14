from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from mr_bean import settings

from .views import SignupView, UserDasboard, UserProfileFormView, UserGallery

app_name = 'users_app'

urlpatterns = [

    # autentication

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),

    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'),
         name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_form_done.html'),
         name='password_change_done'),
    path('password-reset', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/<uidb64>/token/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    #  user side

    path('dashboard/', UserDasboard.as_view(), name='dashboard'),
    path('user-profile-form/',
         UserProfileFormView.as_view(), name='user_profile_form'),
    path('user-gallery/', UserGallery.as_view(), name='user_gallery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
