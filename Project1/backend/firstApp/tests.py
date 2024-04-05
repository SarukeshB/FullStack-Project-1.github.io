import os
import json
import logging
from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class UserSignupLoginTestCase(APITestCase):
    def test_user_signup(self):
        url = reverse('signup')  
        data = {'username': 'testuser', 'password': 'password123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
        self.assertEqual(User.objects.count(), 1)

    def test_user_login(self):
        self.test_user_signup()  
        url = reverse('login') 
        data = {'username': 'testuser', 'password': 'password123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)  

