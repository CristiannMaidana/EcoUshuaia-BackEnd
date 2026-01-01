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

    # GET /api/horario_recoleccion/horario_inicio/06:00:00/horario_fin/12:00:00
    @action(detail=False, methods=['get'], url_path=r'horario_inicio/(?P<inicio>\d{2}:\d{2}:\d{2})/horario_fin/(?P<fin>\d{2}:\d{2}:\d{2})')
    def horarios(self, request, inicio, fin):
        vals = (((HorariosRecoleccion.objects
                .filter(hora_inicio__range=(inicio, fin), hora_inicio__lt=fin)
                .values('id_categoria_residuo'))
                .distinct())
                .order_by('id_categoria_residuo'))
        return Response(list(vals))

    # GET /api/horario_recoleccion/dia/1/zona/1
    @action(detail=False, methods=['get'], url_path=r'dia/(?P<dia>[0-6])/zona/(?P<zona>[0-6])')
    def dia_zona(self, request, dia, zona):
        vals = (HorariosRecoleccion.objects
                .filter(id_zona=int(zona), dia_semana=(dia))
                .values('id_categoria_residuo')
                .distinct())
        return Response(list(vals))

    # GET /api/horario_recoleccion/horario_inicio/06:00:00/dia_mannana/1/zona_id/1
    @action(detail=False, methods=['get'], url_path=r'dia_mannana/(?P<mannana>[0-6])/zona_id/(?P<zona>[0-6])')
    def mannana_zona(self, request, mannana, zona):
        vals = (HorariosRecoleccion.objects
                .filter(id_zona=int(zona), dia_semana=int(mannana))
                .distinct()
                .values('id_categoria_residuo', 'id_zona'))
        return Response(list(vals))

    # GET /api/horario_recoleccion/semana/1/zona/1
    @action(detail=False, methods=['get'], url_path='semana/(?P<dia>[0-6])/zona/(?P<zona>[0-6])')
    def semana_zona(self, request, dia, zona):
        vals = (HorariosRecoleccion.objects
                .filter(id_zona=int(zona),  dia_semana__gt=int(dia), dia_semana__lte=6)
                .values('id_categoria_residuo', 'hora_inicio', 'dia_semana', 'id_zona')
                .distinct()
                .order_by('id_categoria_residuo'))
        return Response(list(vals))