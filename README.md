# GIS Feature Collection

This README documents steps that are necessary to get the GIS Feature Collection application up and running.

## Configurations
This project relies on configuration file and environment variables to customize its behavior. 
### Environment variables configuration
The environment variable used are:

- **`POSTGRES_DB`**: PostgreSQL database name

- **`POSTGRES_USER`**: PostgreSQL username

- **`POSTGRES_PASSWORD`**: PostgreSQL password

- **`DB_HOST`**: Database host

- **`DB_PORT`**: Database port

- **`DB_ENGINE`**: Database engine

- **`GEOJSON_PATH`**: Path to GeoJSON file path


## Project setup

### Run manually ###

| Steps                                   |          Description                                                                  |
|-----------------------------------------|---------------------------------------------------------------------------------------|
|Take `git clone` from repo                |  take a git clone from the present repository                | 
|Configure environment                          |  Database connection details to be added as environment variables, PostgreSQL database is used in this project                            |
|Run `cd webapp/geofeatures/`        |  Change directory to where the Django application is present                                                                 |
|Run `python manage.py makemigrations`        |  Run command to create migration script automatically (run it every time there is change in the database tables schema)                                                                 |
|Run `python manage.py migrate`        |  Run command to incorporate the migration script so the changes reflect in the DB
|Run `python manage.py createsuperuser`        |  Run command to create Django's superusers in DB                                                                 |                                                                 |
|Run `python manage.py runserver`        |  Run Django server                                                                 |
|Run `python manage.py shell`        |  Run Django shell                                                                 |


### Run with docker ###

| Steps                                 |          Description                                                                  |
|---------------------------------------|---------------------------------------------------------------------------------------|
|Take `git clone` from repo              |  take a git clone from the above repository and checkout to dev branch                |
|Configure environment                          |  Database connection details to be added as environment variables, PostgreSQL database is used in this project                            |
|Run command `docker compose up -d`     |  this command will first create a docker image of the project, spool up a container inside which the application will run|
|Run `docker compose exec gisweb python manage.py makemigrations`        |  Run command to create migration script automatically (run it every time there is change in the database tables schema)                                                                 |
|Run `docker compose exec gisweb python manage.py migrate`        |  Run command to incorporate the migration script so the changes reflect in the DB
|Run `docker compose exec gisweb python manage.py createsuperuser`        |  Run command to create Django's superusers in DB                                                                 |                                                                 |


## Folder structure ###
The project is organized into various folders and files, each serving a specific purpose. Below is an overview of the project structure:

- ****`webapp/`****: 
  - ****`geofeatures/`****:
  	- ***`geofeatures/`***: contains the main Django project files
		- *`asgi.py`*: Configures the Asynchronous Server Gateway Interface entry point for the project
		- *`settings.py`*: main configuration settings for the Django project
		- *`urls.py`*: URL routing configuration for the Django project corresponding to views across all apps.
		- *`wsgi.py`*:  Configures the Web Server Gateway Interface entry point for the project.
	- ***`features/`***: This directory contains the Django app
		- *`admin.py`*: configuration for the Django admin interface for the features app
		- *`apps.py`*: configuration for the features app
		- *`models.py`*: model definitions for the features app
		- *`serializers.py`*: serializers for the features app
		- *`urls.py`*: URL routing configuration for the features app
		- *`views.py`*: view functions or classes for the features app
	- ***`manage.py`***: command-line utility to interact with Django project
  - ****`Dockerfile`****: To create docker image for Django microservice with DB connection
  - ****`load_data.py`****: A script to load initial data into Django application involving loading data from a file and making API calls to populate the database.
  - ****`requirements.txt`****: file listing all the Python dependencies required by your Django project

- ****`sample.env`****: Example .env file

- ****`.gitignore`****: To ignore confidential files

- ****`README.md`****: Documentation for developers

- ****`docker-compose.yml`****: To create docker containers
