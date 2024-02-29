from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class HelloApiView(APIView):
    """Test API View"""
    # serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
