# coding=utf-8
import json
from pprint import pprint
from unittest import skip

from django.test import TestCase
from rest_framework.renderers import JSONRenderer
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from BestPlaces.outputModels import Address
from BestPlaces.placesApiHandler import PlacesApiHandler
from BestPlaces.serializers import MinimalPlaceSerializer
from models import User
from rest_framework.authtoken.models import Token


class PlacesTest(TestCase):
    def setUp(self):
        self.controller = PlacesApiHandler()

    def test_search_places(self):
        response = self.controller.search_place(query="Pizza in Karlsruhe")
        pprint(response)
        self.assertIsNotNone(response)

    def test_serializing(self):
        response = self.controller.search_place(query="Pizza in Karlsruhe")
        serializer = MinimalPlaceSerializer(many=True, data=response)
        serializer.is_valid()
        json = JSONRenderer().render(serializer.data)
        print(json)
        self.assertIsNotNone(serializer.data)

    def test_get_place_information(self):
        response = self.controller.get_place(place_id="ChIJlTaoHkgGl0cRxoI4A0I-HYk")
        self.assertEqual(response.name, "Kais Pizza Brückenrestaurant mit Lieferservice")

    def test_create_adress(self):
        jsonString = '[ { "long_name": "1", "short_name": "1", "types": [ "street_number" ] }, { "long_name": "Fritz-Erler-Straße", "short_name": "Fritz-Erler-Straße", "types": [ "route" ]}, { "long_name": "Innenstadt-Ost", "short_name": "Innenstadt-Ost", "types": [ "sublocality_level_1", "sublocality", "political" ] }, { "long_name": "Karlsruhe", "short_name": "Karlsruhe", "types": [ "locality", "political" ] }, { "long_name": "Karlsruhe", "short_name": "KA", "types": [ "administrative_area_level_2", "political" ] }, { "long_name": "Baden-Württemberg", "short_name": "BW", "types": [ "administrative_area_level_1", "political" ] }, { "long_name": "Germany", "short_name": "DE", "types": [ "country", "political" ] }, { "long_name": "76133", "short_name": "76133", "types": [ "postal_code" ] } ]'
        array = json.loads(jsonString)
        addressJson = Address(array=array)
        address = Address(house_number=1, street="Fritz-Erler-Straße", town="Karlsruhe", zip_code=76133)
        self.assertEqual(addressJson.zipCode, address.zipCode)
        self.assertEqual(addressJson.streetNumber, address.streetNumber)
        self.assertEqual(addressJson.town, address.town)
        self.assertEqual(addressJson.zipCode, address.zipCode)


class APITestCaseUser(APITestCase):
    def setUp(self):
        User.objects.create_user("test", "test@test.de", "Test", "Test", "Test", "Test")
        self.token = Token.objects.get_or_create(user="test")[0].key
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)


class PlacesInterfaceTest(APITestCaseUser):
    def test_search_place_with_location(self):
        response = self.client.get("/place/search?q=Pizza&location=Karlsruhe")
        print(response)
        self.assertEqual(200, response.status_code)

    def test_search_place_with_geo(self):
        response = self.client.get("/place/search?q=Pizza%20in%20Karlsruhe&lat=49.0088981&long=8.410513600000002")
        self.assertEqual(200, response.status_code)

    def test_search_place_without_location(self):
        response = self.client.get("/place/search?q=Pizza%20in%20Karlsruhe")
        self.assertEqual(200, response.status_code)

    def test_search_place_next_page(self):
        response = self.client.get("/place/search?q=Pizza%20in%20Karlsruhe&pt=CvQB6QAAAA_-AN1KWX5fPAohM2uHUUXc7oAhMm405EzDay3vreIgjgkgFfrscLt345IiagvEHwzIiAaL1Or-X9-UHJkg3Ua-N-u-TVDr82WhbyirSYYqOSVnH6jsRMRHvr32tebg60GZqGj5nOxOjsOmTmMhuZeq6fhdSLV1GiIFnfrYf05SP0CG45L8E64OVL11RAh05hDPTA7z0kVY4OBA9LGKvc-65I60IxdlBPrg1qh3Uj2fSllaQ40k4tvz3WttWQIv87exG4xvWe49ACXJxTKKRpRySLD2uYDCquDD4_6y0LSsZdFgFC8u6lFTBCFT_5fGRhIQ5x7fSX2rMjrllbN-4H7i2hoUDEZNzi9SrnhS_ehf9u6IEdSQ91E")
        self.assertEqual(200, response.status_code)

    def test_get_place(self):
        response = self.client.get("/place/ChIJlTaoHkgGl0cRxoI4A0I-HYk/")
        self.assertEqual(200, response.status_code)

class UserTest(APITestCaseUser):
    def test_create_User(self):
        user = {
            'username': 'kolbmarco',
            'password': '1234',
            'email': 'kolb.marco@live.de',
            'first_name': 'Marco',
            'last_name': 'Kolb',
            'hometown': 'Hambrücken',
        }
        response = self.client.post("/user/", data=user, format="json")
        self.assertEqual(201, response.status_code)

    def test_editUserData(self):
        user = {
            'email': 'kolb.marco@gmail.com',
        }
        response = self.client.patch("/user/test/", data=user, format="json")
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.data["email"], "kolb.marco@gmail.com")

    def test_check_username(self):
        response = self.client.get("/user/kolbma/")
        self.assertEquals(404, response.status_code)

    def test_login(self):
        response = self.client.post("/api-token-auth/", data={'username': 'test', 'password': 'Test'}, format="json")
        self.assertEquals(200, response.status_code)
        self.assertEqual(self.token, response.data["token"])

    def test_delete_user(self):
        response = self.client.delete("/user/kolbma/")
        self.assertEquals(404, response.status_code)

