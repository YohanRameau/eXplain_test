from django.shortcuts import get_object_or_404

from territory_api.models import Territory
from territory_api.serializers import TerritorySerializer
from rest_framework import viewsets
from rest_framework.response import Response

class TerritoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving territory.
    """
    def list(self, request):
        queryset = Territory.objects.all()
        serializer = TerritorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Territory.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = TerritorySerializer(user)
        return Response(serializer.data)