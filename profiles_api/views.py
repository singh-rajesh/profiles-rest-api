from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, Format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
        'Uses HTTP methods as function(get, post, patch, put, delete)',
        'Its similar to a traditional Django view',
        'Gives you the most control over your application logic',
        'Its mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
