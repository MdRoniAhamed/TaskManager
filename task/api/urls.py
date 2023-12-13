from django.urls import path,include
from .views import manage, Update
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('manage',manage, basename='manage')
router.register('update', Update, basename='update')

urlpatterns = [
    path('',include(router.urls)),
]
