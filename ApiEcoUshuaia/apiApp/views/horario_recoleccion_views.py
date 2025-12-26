from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from apiApp.models import HorariosRecoleccion
from apiApp.serializers.horario_recoleccion_serializer import HorarioRecoleccionSerializer


class HorarioRecoleccionViewSet(viewsets.ModelViewSet):
    queryset = HorariosRecoleccion.objects.all()
    serializer_class = HorarioRecoleccionSerializer

    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ('id_horario_recoleccion', 'dia_semana' 'hora_inicio')

    # GET /api/horarios-recoleccion/horario_inicio=06:00:00/dia_semana=1/zona_id=1
    @action(detail=False, methods=['get'], url_path=r'horario_inicio/(?P<hhmmss>\d{2}:\d{2}:\d{2})/dia_semana/(?P<dia>[0-6])/zona_id/(?P<zona>[0-6])')
    def horario_dia_zona(self, request, hhmmss, dia, zona):
        vals = (HorariosRecoleccion.objects
                .filter(id_zona=int(zona), dia_semana=int(dia), hora_inicio=hhmmss)
                .values_list('id_categoria_residuo', flat=True))
        return Response(list(vals))