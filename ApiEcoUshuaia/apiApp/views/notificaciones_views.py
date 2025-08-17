from rest_framework import viewsets, filters

from apiApp.models import Notificaciones
from apiApp.serializers.notificaciones_serializer import NotificacionesSerializer


class NotificacionesViewSet(viewsets.ModelViewSet):
    queryset = Notificaciones.objects.all()
    serializer_class = NotificacionesSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('fecha_envio', 'tipo_notificacion')
    ordering_fields = ('fecha_envio', 'tipo_notificacion')