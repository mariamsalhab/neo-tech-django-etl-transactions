Neo Tech Project
Overview
This project is a Django-based application designed to handle client and transaction data. The solution includes an ETL process that extracts client data from a CSV file and transaction data from an Excel file, processes it, and stores it in a PostgreSQL database. A secure API is provided to fetch transaction data based on client_id and an optional date range. The project is Dockerized to facilitate deployment and easy setup.

Project Structure
neo_tech_project/
│
├── neo_tech_project/
│   ├── settings.py           # Django settings
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI config
│   ├── asgi.py               # ASGI config
│
├── transactions/
│   ├── models.py             # Database models (Client, Transaction)
│   ├── views.py              # API views
│   ├── serializers.py        # Data serializers
│   ├── admin.py              # Admin configuration
│   ├── etl.py                # ETL process for data extraction and loading
│   ├── tests.py              # Unit tests (empty currently)
│
├── Dockerfile                # Dockerfile for building the app
├── docker-compose.yml        # Docker Compose configuration
├── manage.py                 # Django manage script
└── requirements.txt          # Python dependencies
Prerequisites
To run this project, you’ll need the following installed on your machine:

Docker
Docker Compose
Setup Instructions
1. Clone the repository
git clone https://github.com/your-repo/neo_tech_project.git
cd neo_tech_project
2. Create .env file
Create a .env file in the root directory to store environment variables like your database credentials. You can include:


POSTGRES_DB=neo_django_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=Mariamsalhab88liu
3. Build and run the application using Docker
Run the following commands to build and start the application:


docker-compose up --build
This will:

Build the Docker image for the Django application.
Start both the Django web service and PostgreSQL database in containers.
Set up a PostgreSQL database named neo_django_db.
Running the ETL Process
The ETL process is defined in the etl.py script. This script extracts data from the clients.csv and transactions.xlsx files, processes it, and loads it into the PostgreSQL database.

To run the ETL process inside the Docker container:

First, ensure your Docker containers are up and running.

Then, execute the following command to run the ETL process:

docker-compose exec web python manage.py runscript etl
This will load the client and transaction data into the database.

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
The API uses JWT (JSON Web Token) for authentication. You will need to provide a valid token in the Authorization header when accessing the API.

To obtain a token, use the following endpoint:

POST /api/token/
Provide the username and password, and you will receive an access token that you can use in your requests.
If you don't have a username and password, you can:

1. Create a superuser using the Django admin panel:
   ```bash
   docker-compose exec server python manage.py createsuperuser

Docker Details
PostgreSQL: The database service is defined in docker-compose.yml as db, and it runs PostgreSQL 16. All data is persisted in a Docker volume called postgres_data.

Web (Django): The web service runs the Django application. It exposes port 8000 and is dependent on the db service. It communicates with the PostgreSQL database using the service name db in the DATABASES setting in settings.py.

Running Migrations
To apply database migrations after modifying models, run:

docker-compose exec web python manage.py migrate
Running Tests
(Currently, no tests are defined.)

To run tests, you would typically use:

docker-compose exec web python manage.py test
Troubleshooting
Common Issues:
Database Connection Error: If you encounter psycopg2.OperationalError: could not translate host name "db" to address, ensure the db service is up and running, and the DATABASES configuration in settings.py is correct.

Missing Migrations: If migrations are not applied, run the migrations manually using the migrate command.

Logs:
You can check the logs of the running containers using:


docker-compose logs
Future Improvements
Add unit tests for API endpoints.
Improve performance in the ETL process using batch inserts.
Enhance API security with rate-limiting.
License
This project is licensed under the MIT License - see the LICENSE file for details.