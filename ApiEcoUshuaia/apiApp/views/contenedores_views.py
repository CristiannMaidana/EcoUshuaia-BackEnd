from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_gis.filters import InBBoxFilter

from apiApp.models import Contenedores
from apiApp.serializers.contenedores_serializer import ContenedoresSerializer


class ContenedoresViewSet(viewsets.ModelViewSet):
    queryset = Contenedores.objects.select_related('id_zona', 'id_residuo', 'id_mapa',).all()
    serializer_class = ContenedoresSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter, InBBoxFilter, )
    search_fields = ('nombre_contenedor', 'id_residuo__nombre')
    ordering_fields = ('nombre_contenedor', 'id_residuo__categoria','id_zona__nombre_zona')
    bbox_filterset_fields = {'coordenada'}
    filterset_fields = {
        'id_residuo': ['exact'],
        'id_zona':    ['exact'],
        'id_mapa':    ['exact'],
    }


    # GET /api/contenedores/filtros/?residuos=1,3,5   (o ?residuos=1&residuos=3&residuos=5)
    @action(detail=False, methods=['get'], url_path=r'filtros')
    def filtros_residuos(self, request):
        # Obtenemos ids de tipo String desde url
        ids = request.query_params.getlist('residuos')
        if len(ids) == 1 and ',' in ids[0]:
            ids = [x.strip() for x in ids[0].split(',') if x.strip()]
        try:
            #Convertimos ids en numero, si no nada
            ids = [int(x) for x in ids]
        except (TypeError, ValueError):
            return Response([])

        # Filtramos los contenedores donde coincidan todos los ids
        qs = self.get_queryset().filter(id_residuo_id__in=ids) if ids else self.get_queryset().none()

        #Serializar el resultado de la query
        ser = self.get_serializer(qs, many=True)
        return Response(ser.data)