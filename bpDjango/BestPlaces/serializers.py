from rest_framework import serializers

from BestPlaces.dbModels import Place, Visit
from BestPlaces.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit