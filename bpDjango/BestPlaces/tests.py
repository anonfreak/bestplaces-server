# coding=utf-8
from pprint import pprint
from unittest import skip

from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from BestPlaces.placesApiHandler import PlacesApiHandler
from models import User
from rest_framework.authtoken.models import Token

class PlacesTest(TestCase):
    def setUp(self):
        self.controller = PlacesApiHandler()

    def test_search_places(self):
        response = self.controller.search_place(query="Pizza in Karlsruhe")
        pprint(response)
        self.assertIsNotNone(response)


class UserTest(APITestCase):
    def setUp(self):
        User.objects.create_user("test", "test@test.de", "Test", "Test", "Test", "Test")
        self.token = Token.objects.get_or_create(user="test")[0].key
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)

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
