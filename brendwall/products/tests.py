from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product


class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product_data = {
            'name': 'Test Product',
            'description': 'This is a test product',
            'price': 100.00
        }

    def test_create_product(self):
        response = self.client.post('/api/products/create/', self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Test Product')

    def test_create_product_invalid_price(self):
        invalid_data = self.product_data.copy()
        invalid_data['price'] = -10  # Неправильная цена
        response = self.client.post('/api/products/create/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Цена должна быть положительным числом.', str(response.data))

    def test_get_product_list(self):
        Product.objects.create(**self.product_data)
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Product')
