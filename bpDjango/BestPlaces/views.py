from rest_framework import viewsets
from rest_framework.views import APIView

from BestPlaces.dbModels import Visit
from BestPlaces.models import User
from BestPlaces.serializers import UserSerializer, PlaceSerializer, VisitSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


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
