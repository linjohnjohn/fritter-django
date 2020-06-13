from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import FreetViewSet
import tweets.views as views

router = DefaultRouter()
router.register('freets', FreetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('create', views.freet_create_view),
    # path('<int:freet_id>/action', views.freet_action_view),
    # path('<int:freet_id>', views.freet_detail_view),
    # path('<int:freet_id>/delete', views.freet_action_view),
]