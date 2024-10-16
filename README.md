Neo Tech Django ETL Transactions Project
#Overview
This project is a Django-based web application designed to manage client and transaction data through an ETL process. It extracts data from CSV and Excel files, processes it, and loads it into a PostgreSQL database. The project also includes a secure API to fetch transaction data based on client_id and an optional date range. The entire project is Dockerized for seamless deployment.

#Project Structure

neo_tech_project/
├── neo_tech_project/
│   ├── settings.py           # Django settings
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI config
│   ├── asgi.py               # ASGI config
├── transactions/
│   ├── models.py             # Database models (Client, Transaction)
│   ├── views.py              # API views
│   ├── serializers.py        # Data serializers
│   ├── admin.py              # Admin configuration
│   ├── etl.py                # ETL process for data extraction and loading
│   ├── tests.py              # Unit tests
├── Dockerfile                # Dockerfile for building the app
├── docker-compose.yml        # Docker Compose configuration
├── manage.py                 # Django manage script
└── requirements.txt          # Python dependencies
#Prerequisites
To run this project, ensure the following are installed on your system:

Docker
Docker Compose
Setup Instructions
Clone the repository
git clone https://github.com/mariamsalhab/neo-tech-django-etl-transactions.git
cd neo-tech-django-etl-transactions
Create a .env file In the root directory, create a .env file for environment variables:

POSTGRES_DB=neo_django_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
Build and run the application using Docker
docker-compose up --build
This will:

#Build the Docker image for the Django app.
Start the PostgreSQL database and the Django web server in containers.
Set up a PostgreSQL database named neo_django_db.
Running the ETL Process
To run the ETL process, which extracts data from the CSV and Excel files and loads it into the database, ensure the containers are running. Then execute:

docker-compose exec web python manage.py runscript etl
This will load the data from clients.csv and transactions.xlsx into the PostgreSQL database.

API Usage
The API provides an endpoint to retrieve transactions based on client_id and an optional date range.

Endpoint
GET /api/transactions/
Parameters:
client_id (required): The ID of the client whose transactions you want to retrieve.
start_date (optional): Start of the date range for filtering transactions.
end_date (optional): End of the date range for filtering transactions.
Example:
GET /api/transactions/?client_id=1&start_date=2023-01-01&end_date=2023-12-31
Authentication:
The API uses JWT authentication. Obtain a token by making a POST request to:
POST /api/token/
You will need a username and password. If not created, run this command to create a superuser:
docker-compose exec server python manage.py createsuperuser
Using the token:
Include the token in your requests:
Authorization: Bearer <your_token>
Database Indexing
Indexing is implemented on the client_id field in the Transaction model for performance optimization.
class Meta:
    indexes = [
        models.Index(fields=['client'], name='idx_client_id'),
    ]
#Running Migrations
To apply database migrations after modifying models, run:

docker-compose exec web python manage.py migrate
Running Tests
To run the tests for the API and other functions, use:
docker-compose exec web python manage.py test
Troubleshooting
Database Connection Error: Ensure the db service is up and running, and verify the DATABASES configuration in settings.py.
Missing Migrations: If migrations are missing, manually run them using the migrate command.
Logs: View logs with:
docker-compose logs
Future Improvements
Celery integration: Use Celery for background ETL processing.
Batch Inserts: Enhance ETL process efficiency by using batch inserts.
#License
This project is licensed under the MIT License. See the LICENSE file for more details.
