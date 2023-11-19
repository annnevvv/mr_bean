from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import SignupView, UserDasboard

app_name = 'users_app'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('dashboard/', UserDasboard.as_view(), name='dashboard')
]
