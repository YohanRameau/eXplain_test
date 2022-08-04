from django.shortcuts import get_object_or_404

from territory_api.models import Territory
from territory_api.serializers import TerritorySerializer
from rest_framework import viewsets
from rest_framework.response import Response

class TerritoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving territory.
    """
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()
    
    