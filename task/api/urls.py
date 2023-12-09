from django.urls import path,include
from .views import manage
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('manage',manage)

urlpatterns = [
    path('',include(router.urls)),
]
