from django.urls import path
from . views import CarViewSet
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register("cars", CarViewSet)

urlpatterns = router.urls
