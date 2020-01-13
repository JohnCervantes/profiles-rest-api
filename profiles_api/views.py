from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API View """

    def get(self, request, format=None):
        """ returns a list of APIView features """
        an_apiview = [
            'uses HTTP methods as functions (get, put ,patch put, delete)',
            'Is similar to a tradition django view',
            'gives you the most control over application logic'
        ]
        return Response({'message':'hello', 'an_apiview': an_apiview})
