from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserDataViewSet

router = DefaultRouter()
router.register(r'user-data', UserDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]