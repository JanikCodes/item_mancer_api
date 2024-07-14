from rest_framework import serializers
from rest_api.models.item.item import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'user']
