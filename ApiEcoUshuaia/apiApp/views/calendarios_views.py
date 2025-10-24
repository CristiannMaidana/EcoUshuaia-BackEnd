from rest_framework import viewsets, permissions
from rest_framework import filters
from apiApp.models import Calendarios
from apiApp.serializers.calendarios_serializer import CalendarioSerializer


class CalendariosViewSet(viewsets.ModelViewSet):
    queryset = Calendarios.objects.all()
    serializer_class = CalendarioSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('fecha',)
    ordering_fields = ('id_calendario', 'fecha', 'hora', 'titulo')