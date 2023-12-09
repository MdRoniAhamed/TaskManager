from django.urls import path, include
from . import views

urlpatterns = [
    path('api/',include('user.api.urls')),
    path('registration/',views.registration, name='registration'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('get_reset_password/',views.get_reset_password, name="get_reset_password"),
    path('reset_password/<str:token>/',views.reset_password, name="reset_password"),
]
