from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profiles_api import serializers, models, permisions
from rest_framework.authentication import TokenAuthentication


class HelloApiView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ returns a list of APIView features """
        an_apiview = [
            'uses HTTP methods as functions (get, put ,patch put, delete)',
            'Is similar to a tradition django view',
            'gives you the most control over application logic'
        ]
        return Response({'message':'hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Create a hello message with out name """
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk=None):
        """ handle updating an object """
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        """ Handle a partial update of an object """
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ test API ViewSet """
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        a_viewset = {
            'uses HTTP methods as functions (get, put ,patch put, delete)',
            'automatically maps to URLS using Routers',
            'provides more functionality with less code'
        }
        return Response({'messge':'hello','viewset':a_viewset})


class UserProfileViewSet(viewsets.ModelViewSet):
     serializer_class = serializers.UserProfileSerializer
     queryset = models.UserProfile.objects.all()
     authentication_classes = (TokenAuthentication,)
     permission_classes = (permisions.UpdateOwnProfile,)
