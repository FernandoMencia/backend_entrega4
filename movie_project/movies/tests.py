from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User as DjangoUser
from rest_framework.authtoken.models import Token
from .models import Director, Movie

class MoviesAPITestCase(APITestCase):
    def setUp(self):
        # Crear usuario de prueba como superusuario
        self.user = DjangoUser.objects.create_superuser(username='testuser', password='testpassword')

        # Generar token para el usuario
        self.token = Token.objects.create(user=self.user)

        # Inicializar cliente de pruebas y establecer token en las credenciales
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Crear datos de prueba (Directores y Películas)
        self.director1 = Director.objects.create(name='Director 1')
        self.director2 = Director.objects.create(name='Director 2')
        self.movie1 = Movie.objects.create(title='Movie 1', director=self.director1)
        self.movie2 = Movie.objects.create(title='Movie 2', director=self.director2)

    def test_authentication(self):
        # Probar acceso a vistas protegidas
        url = reverse('director-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crud_operations_movies(self):
        url = reverse('movie-list')

        # Crear película
        data = {'title': 'New Movie', 'director': self.director1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Obtener lista de películas
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'New Movie')

        # Actualizar película
        movie_id = response.data[0]['id']
        update_data = {'title': 'Updated Movie', 'director': self.director2.id}
        url_detail = reverse('movie-detail', args=[movie_id])
        response = self.client.put(url_detail, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Movie')

        # Borrar película
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_crud_operations_directors(self):
        url = reverse('director-list')

        # Crear director
        data = {'name': 'New Director'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Obtener lista de directores
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'New Director')

        # Actualizar director
        director_id = response.data[0]['id']
        update_data = {'name': 'Updated Director'}
        url_detail = reverse('director-detail', args=[director_id])
        response = self.client.put(url_detail, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Director')

        # Borrar director
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
