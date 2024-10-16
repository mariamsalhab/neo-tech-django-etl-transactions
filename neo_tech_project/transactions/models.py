from django.db import models

class Client(models.Model):
    client_id = models.CharField(max_length=100, primary_key=True)  # Unique client ID
    name = models.CharField(max_length=255)  # Client's full name
    email = models.EmailField()  # Client's email address
    date_of_birth = models.DateField()  # Date of birth
    country = models.CharField(max_length=100)  # Country of residence
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)  # Current balance

    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100, primary_key=True)  # Unique transaction ID
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Refers to the Client model
    transaction_type = models.CharField(max_length=10)  # 'buy' or 'sell'
    transaction_date = models.DateField()  # Date of the transaction
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Transaction amount
    currency = models.CharField(max_length=10)  # Transaction currency (e.g., USD, EUR)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} {self.currency}"
        
    class Meta:
            indexes = [
                models.Index(fields=['client'], name='idx_client_id'),
            ]


