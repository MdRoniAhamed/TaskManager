from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView
from . import views
from . import signals

urlpatterns = [
    path('register/',RegisterView.as_view(), name='auth_register'),
    path('change_password/',views.change_password, name='change_password'),
    path('login/',obtain_auth_token, name='api_login'),
    path('logout/',views.LogoutView.as_view(), name='api_logout'),
    path('password_reset/',include('django_rest_passwordreset.urls', namespace="password_reset")), 
]
