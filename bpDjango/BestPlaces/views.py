# -*- coding: utf-8 -*-
import os

from django.http import JsonResponse, HttpResponse
from rest_framework import authentication, permissions
from rest_framework import mixins
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from BestPlaces.dbModels import Visit
from BestPlaces.models import User
from BestPlaces.outputModels import create_geo_dict
from BestPlaces.placesApiHandler import PlacesApiHandler
from BestPlaces.serializers import UserSerializer, VisitSerializer, MinimalPlaceSerializer, \
    FullPlaceSerializer


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_google_api_key(request):
    return HttpResponse(content=os.environ["PLACES_API_KEY"], content_type="text/plain")


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VisitViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Visit.objects.order_by('visittime')
    serializer_class = VisitSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Visit.objects.all().filter(user=self.request.user).order_by('-visittime')

# def list(self, request, *args, **kwargs):
#     user = self.request.user
#     visits = Visit.objects.filter(user=user)
#     serializer = VisitSerializer(visits, many=True)
#     if serializer.validate():
#         return Response(serializer.data)
#     else:
#         return Response(status=404)




class PlacesView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    gmaps = PlacesApiHandler()

    def get(self, request, placeId):
        result = self.gmaps.get_place(placeId)
        serializer = FullPlaceSerializer(result)
        return JsonResponse(data=serializer.data, status=200)

    def put(self, request, pk, format=None):
        pass

    def delete(self, request, pk, format=None):
        pass


class SearchView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    gmaps = PlacesApiHandler()

    def get(self, request):
        query = request.query_params.get("q")
        long = request.query_params.get("long")
        lat = request.query_params.get("lat")
        rad = request.query_params.get("rad")
        location = request.query_params.get("location")
        pt = request.query_params.get("pt")
        if location is None:
            geo = create_geo_dict(lat, long)
        if lat is not None:
            location = geo
        elif location is not None:
            query = query + u' in ' + location
        results = self.gmaps.search_place(query=query, location=location, radius=rad, pagetoken=pt)
        serializer = MinimalPlaceSerializer(data=results, many=True)
        serializer.is_valid()
        json = {"pagetoken": self.gmaps.get_pagetoken(), "results": serializer.data}
        response = Response(data=json, status=200)
        return response

    def put(self, request, pk, format=None):
        pass

    def delete(self, request, pk, format=None):
        pass
