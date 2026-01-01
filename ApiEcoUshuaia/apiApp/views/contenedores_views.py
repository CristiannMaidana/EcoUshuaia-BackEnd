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

    # Helper para el paso a lista de ints
    def _helper_int_ids(self, request, param_name: str):
        raw = request.query_params.getlist(param_name)

        if not raw:
            return []

        # Caso: ['1,2,3']
        if len(raw) == 1 and ',' in raw[0]:
            raw = [x.strip() for x in raw[0].split(',') if x.strip()]
        else:
            raw = [x.strip() for x in raw if x.strip()]

        try:
            return [int(x) for x in raw]
        except (TypeError, ValueError):
            return None

    #Helper para devolver estados invalidos
    def _response_if_invalid_ids(self, ids):
        return Response([]) if ids is None else None

    # GET /api/contenedores/filtros/?residuos=1,3,5   (o ?residuos=1&residuos=3&residuos=5)
    @action(detail=False, methods=['get'], url_path=r'filtros')
    def filtros_residuos(self, request):
        # Obtenemos ids de tipo String desde url
        ids = self._helper_int_ids(request, 'residuos')
        invalid = self._response_if_invalid_ids(ids)
        if invalid:
            return invalid

        # Filtramos los contenedores donde coincidan todos los ids
        qs = self.get_queryset().filter(id_residuo_id__in=ids) if ids else self.get_queryset().none()

        #Serializar el resultado de la query
        ser = self.get_serializer(qs, many=True)
        return Response(ser.data)

    # GET /api/contenedores/por-categorias/?categorias=2,3,4,5
    @action(detail=False, methods=['get'], url_path=r'por-categorias')
    def por_categorias(self, request):
        #obtenemos ids de tipo String desde url
        ids = self._helper_int_ids(request, 'categorias')
        invalid = self._response_if_invalid_ids(ids)
        if invalid:
            return invalid

        qs = (self.get_queryset()
              .filter(id_residuo__id_categoria_residuos__in=ids)
              .order_by('id_residuo__nombre')) if ids else self.get_queryset().none()

        #Serializar el resultado de la query
        ser = self.get_serializer(qs, many=True)
        return Response(ser.data)