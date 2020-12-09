from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet

from profiles_api import serializers

class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, Format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
        'Uses HTTP methods as function(get, post, patch, put, delete)',
        'Its similar to a traditional Django view',
        'Gives you the most control over your application logic',
        'Its mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'Method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""

        return Response({'Method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle a partial update of an object"""

        return Response({'Method': 'DELETE'})

class HelloViewSet(ViewSet):
    """Test API Viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello Message"""

        a_viewset = [
        'Uses actions (list, create, retrieve, update, partial_update)',
        'Automatically maps URLs using routers',
        'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello','a_viewset': a_viewset})

    def create(self, request):
        """Create a new Hello Message"""

        serializer = self.serializer_class(data.request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Retrive an object by it's ID"""

        return Response({'HTTP Method': 'GET'})

    def update(self, request, pk=None):
        """Updates an object by it's ID"""

        return Response({'HTTP Method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Partial updates an object by it's ID"""

        return Response({'HTTP Method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Remove an object by it's ID"""

        return Response({'HTTP Method': 'DELETE'})
