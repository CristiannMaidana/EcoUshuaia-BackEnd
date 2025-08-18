from rest_framework import viewsets, filters

from apiApp.models import Direcciones


class DireccionesViewSet(viewsets.ModelViewSet):
    queryset = Direcciones.objects.all()
    serializer_class = Direcciones

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('calle',)
    ordering_fields = ('id_direccion', 'barrio', 'calle')