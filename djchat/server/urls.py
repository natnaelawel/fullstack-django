from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ServerListViewSet

router = DefaultRouter()
router.register(r"select", ServerListViewSet, basename="server")

urlpatterns = [
] + router.urls
