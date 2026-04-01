from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny

from apiApp.models import Direcciones
from apiApp.serializers.direcciones_serializer import DireccionSerializer


class DireccionesViewSet(viewsets.ModelViewSet):
    queryset = Direcciones.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [AllowAny]

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('calle',)
    ordering_fields = ('id_direccion', 'barrio', 'calle')