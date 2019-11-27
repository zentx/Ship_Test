from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_mongoengine import viewsets as meviewsets

from Mongo_API.Crud_API.serializers import ShipSerializer
from Mongo_API.Crud_API.models import Ship

# Create your views here.

class ShipViewSet(APIView):
    
    def get(self, request, id):
        serializer = ShipSerializer(Ship.objects.get(_id=id))
        response = {"ships": serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        data = request.data
        ship = Ship.objects.get(_id=id)
        serializer = ShipSerializer(ship, data=data)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)
