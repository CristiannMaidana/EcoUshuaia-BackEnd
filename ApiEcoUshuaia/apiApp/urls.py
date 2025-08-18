from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apiApp.views.calendarios_views import CalendariosViewSet
from apiApp.views.contenedores_views import ContenedoresViewSet
from apiApp.views.coordenada_views import CoordendaViewSet
from apiApp.views.notificaciones_views import NotificacionesViewSet
from apiApp.views.residuos_views import ResiduosViewSet
from apiApp.views.ususarios_views import UsuariosViewSet

router = DefaultRouter()
router.register('residuos', ResiduosViewSet, basename='residuos')
router.register('calendarios', CalendariosViewSet, basename='calendarios')
router.register('coordenadas', CoordendaViewSet, basename='coordenadas')
router.register('notificaciones', NotificacionesViewSet, basename='notificaciones')
router.register('usuarios', UsuariosViewSet, basename='usuarios')
router.register('contenedores', ContenedoresViewSet, basename='contenedores')
urlpatterns = [
    path('', include(router.urls)),
]