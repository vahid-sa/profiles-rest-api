from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of API View features"""
        an_apiview = [
            "Uses HTTP method as function (get, post, put, patch, delete)",
            "Is similar to a traditional Django View",
            "Gives you most control over your application logic",
            "Is mapped manually to URLs",
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

