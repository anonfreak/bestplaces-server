from rest_framework import serializers

from BestPlaces.dbModels import Place, Visit
from BestPlaces.models import User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        return get_user_model().objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["first_name"],
            validated_data["last_name"],
            validated_data["hometown"],
            validated_data["password"]
        )

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name', "hometown","password")

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit