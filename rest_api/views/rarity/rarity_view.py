from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_api.models.rarity.rarity import Rarity
from rest_api.serializers.rarity.rarity_serializer import RaritySerializer
from rest_framework import viewsets

class RarityViewSet(viewsets.ModelViewSet):
    queryset = Rarity.objects.all()
    serializer_class = RaritySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # automatically set the user based on the authenticated user
        serializer.save(user=self.request.user)

class RarityUserOverview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        items = Rarity.objects.filter(user=user)
        serializer = RaritySerializer(items, many=True)
        return Response(serializer.data)