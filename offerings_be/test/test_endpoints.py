from rest_framework import status
from django.conf import settings

from rest_framework.test import APITestCase


from offerings_be.offerings.views import OfferingsViewSet

class Test_Offerings(APITestCase):

   def test_get(self):
       #url = reverse_lazy('offerings')
       response = self.client.get('/api/v1/offerings/')

       self.assertEqual(response.status_code, status.HTTP_200_OK)


class Test_Profile(APITestCase):

    def test_get(self):

        response = self.client.get('/api/v1/profile/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class Test_Users(APITestCase):

    def test_get(self):

        response = self.client.get('/api/v1/users/')

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)