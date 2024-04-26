# customer_management
managing customer information.
# Customer Relationship Management API

This Django project implements a RESTful API for managing customer information, businesses, locations, and their relationships.

## Features

- CRUD operations for customers, businesses, locations and customer-business-locations
- Managing relationships between customers,business and location
- RESTful API endpoints for creating, retrieving, updating, and deleting data

## Endpoints

### Customer API Endpoints

- **Create a customer:** `POST /api/customers/`
- **Retrieve all customers:** `GET /api/customers/`
- **Retrieve a specific customer:** `GET /api/customers/<customer_id>/`
- **Update a customer:** `PUT /api/customers/<customer_id>/`
- **Partial update of a customer:** `PATCH /api/customers/<customer_id>/`
- **Delete a customer:** `DELETE /api/customers/<customer_id>/`

### Business API Endpoints

- **Create a business:** `POST /api/businesses/`
- **Retrieve all businesses:** `GET /api/businesses/`
- **Retrieve a specific business:** `GET /api/businesses/<business_id>/`
- **Update a business:** `PUT /api/businesses/<business_id>/`
- **Partial update of a business:** `PATCH /api/businesses/<business_id>/`
- **Delete a business:** `DELETE /api/businesses/<business_id>/`

### Location API Endpoints

- **Create a location:** `POST /api/locations/`
- **Retrieve all locations:** `GET /api/locations/`
- **Retrieve a specific location:** `GET /api/locations/<location_id>/`
- **Update a location:** `PUT /api/locations/<location_id>/`
- **Partial update of a location:** `PATCH /api/locations/<location_id>/`
- **Delete a location:** `DELETE /api/locations/<location_id>/`

### Customer-Business-locations Relationship API Endpoints

- **Create a customer-business relationship:** `POST /api/customer-business-location/`
- **Retrieve all customer-business relationships:** `GET /api/customer-business-location/`
- **Retrieve a specific customer-business relationship:** `GET /api/customer-business-location/<relationship_id>/`
- **Update a customer-business relationship:** `PUT /api/customer-business-location/<relationship_id>/`
- **Partial update of a customer-business relationship:** `PATCH /api/customer-business-location/<relationship_id>/`
- **Delete a customer-business relationship:** `DELETE /api/customer-business-location/<relationship_id>/`

## Setup

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Apply database migrations using `python manage.py migrate`.
4. Start the development server using `python manage.py runserver`.
5. Access the API endpoints using the provided URLs.

## Technologies Used

- Django
- Django REST Framework
- Swagger UI

## License

This project is licensed under the [MIT License](LICENSE).

