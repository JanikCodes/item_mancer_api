from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_api.models.item import Item
from rest_api.serializers import ItemSerializer

class ItemUserOverview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        items = Item.objects.filter(user=user)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)