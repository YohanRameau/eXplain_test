from django.urls import path

from territory_api.views import TerritoryViewSet

urlpatterns = [
    path('/', TerritoryViewSet.as_view(), name='territory')
]
