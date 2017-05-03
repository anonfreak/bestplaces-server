from django.http import Http404
from rest_framework import generics, status
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from BestPlaces.dbModels import Visit
from BestPlaces.models import User
from BestPlaces.serializers import UserSerializer, PlaceSerializer, VisitSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
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
        query = request.query_params.get("q")
        long = request.query_params.get("long")
        lat = request.query_params.get("lat")
        rad = request.query_params.get("rad")
        location = request.query_params.get("location")



    def put(self, request, pk, format=None):
        pass

    def delete(self, request, pk, format=None):
        pass
