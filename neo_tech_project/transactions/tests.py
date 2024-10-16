from django.test import TestCase

from rest_framework.test import APIClient
from django.urls import reverse
from transactions.models import Client, Transaction

class ClientTransactionTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Create a sample client and transaction for testing
        self.client_obj = Client.objects.create(
            client_id='1',
            name='John Doe',
            email='john@example.com',
            date_of_birth='1990-01-01',
            country='USA',
            account_balance=1000.00
        )

        self.transaction_obj = Transaction.objects.create(
            transaction_id='1',
            client=self.client_obj,
            transaction_type='buy',
            transaction_date='2024-01-01',
            amount=500.00,
            currency='USD'
        )

    def test_get_transactions(self):
        # Test fetching client transactions
        response = self.client.get(f'/api/clients/{self.client_obj.client_id}/transactions/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'buy')

    def test_get_transactions_with_date_range(self):
        # Test fetching transactions with a date range
        response = self.client.get(f'/api/clients/{self.client_obj.client_id}/transactions/?start_date=2024-01-01&end_date=2024-12-31')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'buy')
