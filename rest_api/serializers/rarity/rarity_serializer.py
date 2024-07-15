from rest_framework import serializers
from rest_api.models.rarity.rarity import Rarity
    
class RaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rarity
        fields = '__all__'

