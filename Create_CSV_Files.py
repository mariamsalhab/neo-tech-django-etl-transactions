import pandas as pd

# Sample data for clients
clients_data = {
    "client_id": [1, 2, 3, 4, 5],
    "name": ["John Doe", "Jane Smith", "Sam Brown", "Emily White", "Michael Black"],
    "email": ["john@example.com", "jane@example.com", "sam@example.com", "emily@example.com", "michael@example.com"],
    "date_of_birth": ["1985-02-15", "1990-06-30", "1978-11-05", "1988-03-22", "1992-08-10"],
    "country": ["USA", "UK", "Canada", "Germany", "Australia"],
    "account_balance": [10000.50, 5000.75, 12000.00, 8500.60, 4500.30]
}

# Creating a DataFrame
clients_df = pd.DataFrame(clients_data)

# Saving to CSV
clients_df.to_csv('clients.csv', index=False)

print("clients.csv file created successfully.")


# Sample data for transactions
transactions_data = {
    "transaction_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "client_id": [1, 2, 1, 3, 2, 4, 5, 3, 4, 5],
    "transaction_type": ["buy", "sell", "buy", "buy", "sell", "buy", "sell", "buy", "sell", "buy"],
    "transaction_date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05", "2024-01-06", 
                         "2024-01-07", "2024-01-08", "2024-01-09", "2024-01-10"],
    "amount": [1000.00, -500.00, 1200.00, 3000.00, -200.00, 1500.00, -700.00, 2500.00, -350.00, 4000.00],
    "currency": ["USD", "USD", "EUR", "USD", "USD", "EUR", "USD", "USD", "EUR", "USD"]
}

# Creating a DataFrame
transactions_df = pd.DataFrame(transactions_data)

# Saving to Excel
transactions_df.to_excel('transactions.xlsx', index=False)

print("transactions.xlsx file created successfully.")
