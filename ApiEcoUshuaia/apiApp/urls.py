from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apiApp.views.calendarios_views import CalendariosViewSet
from apiApp.views.coordenada_views import CoordendaViewSet
from apiApp.views.notificaciones_views import NotificacionesViewSet
from apiApp.views.residuos_views import ResiduosViewSet

router = DefaultRouter()
router.register('residuos', ResiduosViewSet, basename='residuos')
router.register('calendarios', CalendariosViewSet, basename='calendarios')
router.register('coordenadas', CoordendaViewSet, basename='coordenadas')
router.register('notificaciones', NotificacionesViewSet, basename='notificaciones')
urlpatterns = [
    path('', include(router.urls)),
]