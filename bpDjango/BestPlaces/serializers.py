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

    def destroy(self, instance):
        instance.delete()

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name', "hometown","password")


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place


class MinimalPlaceSerializer(serializers.Serializer):
    placeId = serializers.CharField()
    name = serializers.CharField()
    geo = serializers.DictField()
    formatted_address = serializers.CharField()
    openNow = serializers.BooleanField()
    rating = serializers.IntegerField()
    photos = serializers.ListField()
    categories = serializers.ListField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit