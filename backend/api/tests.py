from django.urls import path, include, reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from api.serializers import ExperimentSerializer, ResultsSerializer
from api.models import Experiment, Results
# Create your tests here.

class UserTests(APITestCase):
    urlpatterns = [
            path('', include('api.urls')),
            path('api-auth/', include('rest_framework.urls')),
        ]
    
    def setUp(self):
        username = 'admin'
        password = 'adminpassword'
        admin = User.objects.create_superuser(username, 'admin@gmail.com', password)
        self.client.login(username=admin, password= password)

    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')    
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

class ExperimentTests(APITestCase):

    urlpatterns = [
        path('', include('api.urls')),
        path('api-auth/', include('rest_framework.urls')),
    ]

    def setUp(self):
        username = 'admin'
        password = 'adminpassword'
        admin = User.objects.create_superuser(username, 'admin@gmail.com', password)
        user = 'user'
        userpassword = 'userpassword'
        user = User.objects.create_user(user, 'user@email.com', userpassword)
        self.client.login(username= user, password = userpassword)
        data = {'title': 'test experiment', 'code': 'print("1, 2, 3 Prova")'}
        url = reverse('experiment-list')
        response = self.client.post(url, data, format='json')
        self.client.logout()
    
    def test_list_experiments(self):
        self.client.login(username = 'user', password = 'userpassword')
        url = reverse('experiment-list')
        response = self.client.get(url, format='json')
        print('''----------------------------------------\n
                response:
                ------------------------------------------\n''', response.data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_experiment(self):
        self.client.login(username = 'user', password = 'userpassword')
        url = reverse('experiment-list')
        data = {'title': 'test experiment', 'code': 'print("1, 2, 3 Prova")'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Experiment.objects.count(), 2)
    
    # def test_run_experiment(self):
    #     self.client.login(username = 'user', password = 'userpassword')
    #     url = reverse('experiment-list')
    #     data = {'title': 'test experiment 2', 'code': 'print("1, 2, 3 Prova")'}
    #     response = self.client.post(url, data, format='json')
    #     print('''----------------------------------------\n
    #           1st response:
    #           ------------------------------------------\n''', response.data)
    #     experiment = self.client.get(response.data['url'],format ='json')
    #     print('''----------------------------------------\n
    #           experiment obj:
    #           ------------------------------------------\n''', experiment.data)
    #     url = reverse('experiment-run', args=[experiment.data["id"]])
    #     response = self.client.post(url)
    #     print('''----------------------------------------\n
    #           2nd response:
    #           ------------------------------------------\n''', response.data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Results.objects.count(), 1)
    #     url = reverse('results-list')
    #     result = self.client.get(url,format ='json')
    #     print('''----------------------------------------\n
    #             result obj:
    #             ------------------------------------------\n''', result.data)
    #     url = reverse('experiment-list')
    #     experiment = self.client.get(url,format ='json')
    #     print('''----------------------------------------\n
    #           experiment obj after run:
    #           ------------------------------------------\n''', experiment.data)
    
        

class ResultsTests(APITestCase):
    pass

