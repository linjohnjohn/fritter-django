from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views

router = DefaultRouter()
router.register('user', UserAPI)

urlpatterns = [
    path('auth/register/', RegisterAPI.as_view()),
    path('auth/login/', LoginAPI.as_view()),
    path('auth', include('knox.urls')),
    path('', include(router.urls)),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='know_logout'),
]