from rest_framework import viewsets, filters

from apiApp.models import HorariosRecoleccion
from apiApp.serializers.horario_recoleccion_serializer import HorarioRecoleccionSerializer


class HorarioRecoleccionViewSet(viewsets.ModelViewSet):
    queryset = HorariosRecoleccion.objects.all()
    serializer_class = HorarioRecoleccionSerializer

    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ('id_horario_recoleccion', 'dia_semana' 'hora_inicio')