from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class UserTest(APITestCase):
    def test_check_username(self):
        url = reverse('checkUsername')
        self.client.credentials(HTTP_AUTHORIZATION="Basic YWRtaW46YWJjMTIzNCE=")
        response = self.client.get("/user?username=kolbma")
        self.assertEqual(response.data, "Test")