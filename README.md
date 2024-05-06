# Customer Relationship Management API

This Django project implements a RESTful API for managing customer information, businesses, locations, and their relationships.

## Features

- CRUD operations for customers, businesses, locations, and customer-business-locations
- Managing relationships between customers, businesses, and locations
- RESTful API endpoints for creating, retrieving, updating, and deleting data

## Authentication

This API uses basic authentication to secure access to its endpoints. To authenticate requests, clients must include an `Authorization` header with a base64-encoded username and password in the format `Basic <credentials>`.

### Obtaining Credentials

To obtain credentials, users can register for an account and provide their username and password. The server verifies the credentials and responds with a token that can be used for subsequent requests.

### Using Credentials

Once a client has obtained credentials, they can include them in the `Authorization` header of their requests to authenticate.

# Database Design Document

# Customer Relationship Management (CRM) API

This Django project implements a RESTful API for managing customer information, businesses, locations, and their relationships.

## Prerequisites

Before setting up and running the CRM API project, ensure that you have the following prerequisites installed and configured:

1. **Python**: Make sure you have Python installed on your system. You can download and install Python from the [official Python website](https://www.python.org/).

2. **Django**: The project is built using the Django web framework.

3. **Database**: Ensure that you have MySQL installed and configured on your system. The project is designed to work with MySQL as the database system. You can download and install MySQL from the [official MySQL website](https://www.mysql.com/).

4. **Git**: Git is used for version control. Make sure you have Git installed on your system to clone the project repository. You can download and install Git from the [official Git website](https://git-scm.com/).

5. **Dependencies**: After cloning the project repository, navigate to the project directory and install the required dependencies listed in the `requirements.txt` file using pip:



## Overview

This document outlines the design of the database for managing customer information, businesses, locations, and their relationships.

## Entity-Relationship Diagram (ERD)

The following ERD illustrates the entities and their relationships in the database:

![ERD](https://github.com/evantoh/customer_management/blob/main/static/images/database.png)

## Entities

### Customer

- **customer_id**: INT (Primary Key)
- **customerName**: VARCHAR(100)
- **phoneNumber**: VARCHAR(20)
- **emailAddress**: VARCHAR(100)
- **dateOfBirth**: DATE
- **nationality**: VARCHAR(50)

### Business

- **business_id**: INT (Primary Key)
- **businessName**: VARCHAR(100)
- **businessCategory**: VARCHAR(100)
- **businessRegistrationDate**: DATE
- **ageOfBusiness**: INT

### Location

- **location_id**: INT (Primary Key)
- **county**: VARCHAR(50)
- **subCounty**: VARCHAR(50)
- **ward**: VARCHAR(50)
- **buildingName**: VARCHAR(100)
- **floor**: VARCHAR(10)

### CustomerBusiness

- **relationship_id**: INT (Primary Key)
- **customer_id**: INT (Foreign Key to Customer)
- **business_id**: INT (Foreign Key to Business)
- **location_id**: INT (Foreign Key to Location)

## Relationships

- One customer can have multiple business relationships (one-to-many)
- One business can have multiple customer relationships (one-to-many)
- Each customer-business relationship is associated with a location (one-to-many)
- Customers can have relationships with multiple businesses and businesses can have relationships with multiple customers (many-to-many)
- A location can host multiple businesses

## Tables

### Customer Table

| Field          | Type         | Null | Key | Default | Extra          |
|----------------|--------------|------|-----|---------|----------------|
| customer_id    | INT          | NO   | PRI | NULL    | AUTO_INCREMENT |
| customerName   | VARCHAR(100) | NO   |     | NULL    |                |
| phoneNumber    | VARCHAR(20)  | YES  |     | NULL    |                |
| emailAddress   | VARCHAR(100) | YES  |     | NULL    |                |
| dateOfBirth    | DATE         | YES  |     | NULL    |                |
| nationality    | VARCHAR(50)  | YES  |     | NULL    |                |

### Business Table

| Field                  | Type         | Null | Key | Default | Extra          |
|------------------------|--------------|------|-----|---------|----------------|
| business_id            | INT          | NO   | PRI | NULL    | AUTO_INCREMENT |
| businessName           | VARCHAR(100) | NO   |     | NULL    |                |
| businessCategory       | VARCHAR(100) | YES  |     | NULL    |                |
| businessRegistrationDate | DATE       | YES  |     | NULL    |                |
| ageOfBusiness          | INT          | YES  |     | NULL    |                |

### Location Table

| Field          | Type         | Null | Key | Default | Extra          |
|----------------|--------------|------|-----|---------|----------------|
| location_id    | INT          | NO   | PRI | NULL    | AUTO_INCREMENT |
| county         | VARCHAR(50)  | YES  |     | NULL    |                |
| subCounty      | VARCHAR(50)  | YES  |     | NULL    |                |
| ward           | VARCHAR(50)  | YES  |     | NULL    |                |
| buildingName   | VARCHAR(100) | YES  |     | NULL    |                |
| floor          | INT          | YES  |     | NULL    |                |

### CustomerBusiness Table

| Field           | Type         | Null | Key | Default | Extra          |
|-----------------|--------------|------|-----|---------|----------------|
| relationship_id | INT          | NO   | PRI | NULL    | AUTO_INCREMENT |
| customer_id     | INT          | YES  |     | NULL    |                |
| business_id     | INT          | YES  |     | NULL    |                |
| location_id     | INT          | YES  |     | NULL    |                |

## Indexes

- Indexes can be added to improve query performance on frequently accessed columns, such as `customer_id`, `business_id`, and `location_id`.

## Endpoints

### Customer API Endpoints

- **Create a customer:** `POST /api/customers/`
- **Retrieve all customers:** `GET /api/customers/`
- **Retrieve a specific customer:** `GET /api/customers/<customer_id>/`
- **Update a customer:** `PUT /api/customers/<customer_id>/`
- **Partial update of a customer:** `PATCH /api/customers/<customer_id>/`
- **Delete a customer:** `DELETE /api/customers/<customer_id>/`

#### Customer API SwaggerUI
![Swagger Documentation](https://github.com/evantoh/customer_management/blob/main/static/images/customers-swagger.png)


### Business API Endpoints

- **Create a business:** `POST /api/businesses/`
- **Retrieve all businesses:** `GET /api/businesses/`
- **Retrieve a specific business:** `GET /api/businesses/<business_id>/`
- **Update a business:** `PUT /api/businesses/<business_id>/`
- **Partial update of a business:** `PATCH /api/businesses/<business_id>/`
- **Delete a business:** `DELETE /api/businesses/<business_id>/`

#### Business API SwaggerUI
![Swagger Documentation](https://github.com/evantoh/customer_management/blob/main/static/images/business-swagger.png)

### Location API Endpoints

- **Create a location:** `POST /api/locations/`
- **Retrieve all locations:** `GET /api/locations/`
- **Retrieve a specific location:** `GET /api/locations/<location_id>/`
- **Update a location:** `PUT /api/locations/<location_id>/`
- **Partial update of a location:** `PATCH /api/locations/<location_id>/`
- **Delete a location:** `DELETE /api/locations/<location_id>/`

#### Location API SwaggerUI
![Swagger Documentation](https://github.com/evantoh/customer_management/blob/main/static/images/location-swagger.png)

### Customer-Business-Locations Relationship API Endpoints

- **Create a customer-business relationship:** `POST /api/customer-business-location/`
- **Retrieve all customer-business relationships:** `GET /api/customer-business-location/`
- **Retrieve a specific customer-business relationship:** `GET /api/customer-business-location/<relationship_id>/`
- **Update a customer-business relationship:** `PUT /api/customer-business-location/<relationship_id>/`
- **Partial update of a customer-business relationship:** `PATCH /api/customer-business-location/<relationship_id>/`
- **Delete a customer-business relationship:** `DELETE /api/customer-business-location/<relationship_id>/`

#### Customer-Business-Locations API SwaggerUI
![Swagger Documentation](https://github.com/evantoh/customer_management/blob/main/static/images/customer-business-location-swagger.png)


## Sample Request
![Swagger Documentation](https://github.com/evantoh/customer_management/blob/main/static/images/sample-request.png)


## Setup

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Apply database migrations using `python manage.py migrate` or `make migrate`.
4. Start the development server using `python manage.py runserver` or `make server`.
5. Run tests using `python manage.py test` or `make test`.
6. Access the API endpoints using the provided URLs.


## Technologies Used

- Django
- Django REST Framework
- Swagger UI

## License

This project is licensed under the [MIT License](LICENSE).
