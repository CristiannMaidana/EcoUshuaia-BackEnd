from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apiApp.views.calendarios_views import CalendariosViewSet
from apiApp.views.categoria_noticias_views import CategoriaNoticiasViewSet
from apiApp.views.contenedores_views import ContenedoresViewSet
from apiApp.views.coordenada_views import CoordendaViewSet
from apiApp.views.direcciones_views import DireccionesViewSet
from apiApp.views.notificaciones_views import NotificacionesViewSet
from apiApp.views.residuos_views import ResiduosViewSet
from apiApp.views.usuarios_historiales_residuos_views import UsuariosHistorialesResiduosViewSet
from apiApp.views.ususarios_views import UsuariosViewSet
from apiApp.views.zonas_views import ZonasViewSet

router = DefaultRouter()
router.register('residuos', ResiduosViewSet, basename='residuos')
router.register('calendarios', CalendariosViewSet, basename='calendarios')
router.register('coordenadas', CoordendaViewSet, basename='coordenadas')
router.register('notificaciones', NotificacionesViewSet, basename='notificaciones')
router.register('usuarios', UsuariosViewSet, basename='usuarios')
router.register('contenedores', ContenedoresViewSet, basename='contenedores')
router.register('zonas', ZonasViewSet, basename='zonas')
router.register('direcciones', DireccionesViewSet, basename='direcciones')
router.register('Historial de residuos de usuarios', UsuariosHistorialesResiduosViewSet, basename='usuariosHistorialesResiduos')
router.register('Registro de contenedores de ususarios', UsuariosHistorialesResiduosViewSet, basename='usuarioRegistroContenedores')
router.register('categoria_noticias', CategoriaNoticiasViewSet, basename='categoriaNoticias')
urlpatterns = [
    path('', include(router.urls)),
]