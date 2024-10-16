import pandas as pd
from psycopg2 import connect

def run_etl():
    # Connect to PostgreSQL
    conn = connect(
        dbname="neo_django_db",
        user="postgres",
        password="Mariamsalhab88liu",
        host="db"
    )
    cur = conn.cursor()

    # Load and insert clients data
    clients = pd.read_csv(r'C:/Users/Mariam Salhab/Desktop/Neo Tech Ass/clients.csv')
    for _, row in clients.iterrows():
        cur.execute(
            "INSERT INTO transactions_client (client_id, name, email, date_of_birth, country, account_balance) VALUES (%s, %s, %s, %s, %s, %s)",
            (row['client_id'], row['name'], row['email'], row['date_of_birth'], row['country'], row['account_balance'])
        )

    # Load and insert transactions data
    transactions = pd.read_excel(r'C:/Users/Mariam Salhab/Desktop/Neo Tech Ass/transactions.xlsx')
    for _, row in transactions.iterrows():
        cur.execute(
            "INSERT INTO transactions_transaction (transaction_id, client_id, transaction_type, transaction_date, amount, currency) VALUES (%s, %s, %s, %s, %s, %s)",
            (row['transaction_id'], row['client_id'], row['transaction_type'], row['transaction_date'], row['amount'], row['currency'])
        )

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    run_etl()
