from rest_framework import serializers
from .models import Territory, TerritoryParents


class TerritorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Territory
        fields = '__all__'

# class TerritoryParentsSerializer(serializers.ModelSerializer):    
#     class Meta:
#         model = Territory
#         fields = '__all__'