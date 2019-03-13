# from rest_framework import status
# from django.conf import settings

# from rest_framework.test import APITestCase


# from offerings_be.offerings.views import OfferingsViewSet
# from offerings_be.offerings.models import Offerings
# from offerings_be.users.models import User


# class Test_Users(APITestCase):

#     def test_get(self):

#         response = self.client.get('/api/v1/users/')

#         self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

#     def test_post(self):

#         test_user = {
#             "id": 1,
#             "user": "6556fbcf-67ae-4818-bcd3-693b94836486",
#             "username": "matt",
#             "password": "matt"
#         }

#         create_user = self.client.post('/api/v1/users/', test_user, format='json')
#         print('Users:', create_user.content)
#         self.assertEqual(create_user.status_code, status.HTTP_201_CREATED)



# class Test_Offerings(APITestCase):

#     def test_get(self):
#        #url = reverse_lazy('offerings')
#        response = self.client.get('/api/v1/offerings/', format='json')

#        self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_post(self):

#         test_user = {
#             "id": 1,
#             "user": "6556fbcf-67ae-4818-bcd3-693b94836486",
#             "username": "matt",
#             "password": "matt"
#         }

#         create_user = self.client.post('/api/v1/users/', test_user, format='json')
        
#         data = {
#             'title': 'Test Offering',
#             'description': 'An offering to test endpoint',
#             'phone': 1111111111,
#             'distance': 2,
#             'notify': True,
#             'image': 'https://gph.is/2n2XYkw',
#             'profile': 1
#         }

#         response = self.client.post('/api/v1/offerings/', data, format='json')
#         print('Users:', test_user)
#         print('Offerings:', response.content)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Offerings.objects.count(), 1)
#         self.assertEqual(Offerings.objects.get().title, 'Test Offering')




# class Test_Profile(APITestCase):

#     def test_get(self):

#         response = self.client.get('/api/v1/profile/')
#         print('Profile:', response.content)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)