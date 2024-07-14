from rest_framework.views import APIView
from rest_framework.response import Response


class ConnectionTestView(APIView):
    def get(self, request, format=None):
        content = {'success': True}
        
        return Response(content)