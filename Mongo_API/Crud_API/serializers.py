from rest_framework_mongoengine import serializers
from Mongo_API.Crud_API.models import Ship

class ShipSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Ship
        fields = ('name', 'model', 'length', 'crew', 'passengers')