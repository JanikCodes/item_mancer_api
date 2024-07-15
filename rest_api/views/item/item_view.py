from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_api.models.item.item import Item
from rest_api.serializers import ItemSerializer
from rest_framework import viewsets

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # automatically set the user based on the authenticated user
        serializer.save(user=self.request.user)

class ItemUserOverview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        items = Item.objects.filter(user=user)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)