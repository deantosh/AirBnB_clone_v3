# AirBnB Clone - The Console

## Table of Contents

1. [Project Overview](#project-overview)  
2. [The Console](#the-console)  
3. [File Storage Engine](#file-storage-engine)  
4. [Database Storage Engine](#database-storage-engine)  
5. [Web Static](#web-static)  
6. [Web Framework](#web-framework)  
7. [RESTful API](#restful-api)  
8. [Web Dynamic](#web-dynamic)  
9. [Deployment](#deployment)  
10. [Environment](#environment)  
11. [Installation](#installation)  
12. [Usage](#usage)  
13. [Bugs](#bugs)  
14. [Authors](#authors)  
15. [License](#license)  

## Project Overview

This project is part of the ALX software engineering curriculum. It involves building a simplified clone of the AirBnB platform. The project is developed in stages: the Console, File Storage, Web Static, Web Framework, RESTful API, and full-stack deployment using Flask, Gunicorn, Nginx, and Docker.

## The Console

The console is a command-line interpreter that allows users to interact with the application's data models. It provides functionalities to create, read, update, and delete instances of various classes.

### Supported Commands:

- `create <class>`: Creates a new instance of a class.  
- `show <class> <id>`: Displays the string representation of an instance.  
- `destroy <class> <id>`: Deletes an instance.  
- `all [<class>]`: Displays all instances, optionally filtered by class.  
- `update <class> <id> <attribute> <value>`: Updates an instance's attribute.  

### Example:

```bash
(hbnb) create User
(hbnb) show User 1234-5678-9012
(hbnb) update User 1234-5678-9012 email "user@example.com"
(hbnb) destroy User 1234-5678-9012
```

## File Storage Engine

The File Storage engine serializes objects to a JSON file and deserializes JSON files back into objects. It is designed for simplicity and ease of use.

### Core methods:

- `all()`: Returns a dictionary of all objects.  
- `new(obj)`: Adds a new object.  
- `save()`: Serializes objects to JSON file.  
- `reload()`: Loads objects from JSON file.  

## Database Storage Engine

Uses MySQL with SQLAlchemy ORM to provide scalable, robust data persistence.

### Configuration via Environment Variables:

- `HBNB_MYSQL_USER` – MySQL username  
- `HBNB_MYSQL_PWD` – MySQL password  
- `HBNB_MYSQL_HOST` – MySQL host (e.g., localhost)  
- `HBNB_MYSQL_DB` – MySQL database name  
- `HBNB_TYPE_STORAGE=db` – Set storage engine to database  

### Features:

- Maps Python classes to tables.  
- Handles relationships (one-to-many, many-to-many).  
- Implements CRUD operations with session management.  

## Web Static

The front-end static website consists of HTML and CSS files that serve as the user interface framework.

### Includes:

- Responsive layout design.  
- Pages for homepage, listings, user profiles, etc.  
- Cross-browser compatibility.  

## Web Framework

Flask is used as the back-end framework to serve dynamic content.

### Features:

- URL routing.  
- Jinja2 templating.  
- Data injection from storage engines.  

## RESTful API

The RESTful API exposes all models through HTTP endpoints.

### Endpoints:

- `/api/v1/<model>/` - Access model data.  
- Supports JSON requests/responses.  
- Methods: GET, POST, PUT, DELETE.  

### Example:

```http
GET /api/v1/users/
POST /api/v1/places/
PUT /api/v1/amenities/123
DELETE /api/v1/reviews/456
```

## Web Dynamic

Enhances the static front-end using JavaScript and jQuery.

### Features:

- AJAX calls for real-time data loading.  
- Interactive forms and filters.  
- Dynamic DOM updates.  

## Deployment

The project deployment includes:

- Docker: Containerizes the application for portability.  
- Gunicorn: Serves the Flask application as a production WSGI server.  
- Nginx: Acts as a reverse proxy and serves static assets.  
- Secure environment variable management.  

### Deployment Steps:

1. Build Docker image.  
2. Run containers.  
3. Configure Nginx to proxy requests.  
4. Monitor logs and scale as necessary.  

## Environment

- **Operating System**: Ubuntu 20.04 LTS  
- **Programming Language**: Python 3.8+  
- **Web Framework**: Flask  
- **Database**: MySQL  
- **ORM**: SQLAlchemy  
- **Web Server**: Nginx  
- **Application Server**: Gunicorn  

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/AirBnB_clone.git
cd AirBnB_clone
pip install -r requirements.txt
```

Set up environment variables and run the console or web app.

## Usage

To start the console:

```bash
./console.py
```

To run the web server:

```bash
HBNB_TYPE_STORAGE=db python3 -m web_flask.0-hbnb
```

## Bugs
No known bugs at this time. 

## Authors
Alexa Orrico - [Github](https://github.com/alexaorrico) / [X](https://twitter.com/alexa_orrico)  
Jennifer Huang - [Github](https://github.com/jhuang10123) / [X](https://twitter.com/earthtojhuang)

Second part of Airbnb: Joann Vuong

AirBnB -- RESTFUL API part
Deantosh Daiddoh - [Github](https://github.com/deantosh) / [X](https://x.com/daiddoh)
Lucky Archibong - [Github](https://github.com/luckys-lnz) / [X](https://x.com/)

## License
Public Domain. No copy write protection. 
