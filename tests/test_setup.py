from faker import Faker

from rest_framework import status
from rest_framework.test import APITestCase

class TestSetUp(APITestCase):
    
    def setUp(self):
        from apps.users.models import Usuario
        
        fake = Faker()
        
        self.login_url= '/login/'
        self.user = Usuario.objects.create_superuser(
            name='Cleotilde',
            last_name='Cleo',
            username=fake.name(),
            password='litio20',  
            email=fake.email()                                 
        )
        
        response = self.client.post(
            self.login_url,
            {
                'username': self.user.username,
                'password':'litio20'
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token=response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        return super().setUp()