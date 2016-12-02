from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.views import APIView

from BestPlaces.dbModels import Visit
from BestPlaces.models import User
from BestPlaces.serializers import UserSerializer, PlaceSerializer, VisitSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VisitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Visit.objects.all().order_by('-date_joined')
    serializer_class = VisitSerializer

class PlacesView(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """

    def get_object(self, pk):
        pass

    def get(self, request, pk, format=None):
        pass

    def put(self, request, pk, format=None):
        pass

    def delete(self, request, pk, format=None):
        pass

class SearchView(APIView):
    def get(self, request, pk, format=None):
        pass

    def put(self, request, pk, format=None):
        pass

    def delete(self, request, pk, format=None):
        pass
