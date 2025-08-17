from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apiApp.views.residuos_views import ResiduosViewSet

router = DefaultRouter()
router.register('residuos', ResiduosViewSet, basename='residuos')
urlpatterns = [
    path('', include(router.urls)),
]