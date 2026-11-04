# E-commerce Microservices

This project demonstrates a simple e-commerce system built using a microservices architecture. It consists of three main services:

1. **User Authentication Service**: Handles user registration and login, providing JWT tokens for authenticated sessions.
2. **Product Management Service**: Manages product information, including creation, updates, and retrieval of product details.
3. **Order Processing Service**: Manages orders, including placing new orders and retrieving user order history.

## Technology Stack

- Backend: Flask (Python)
- Database: SQLite for simplicity and demonstration purposes (can be replaced with any SQL database)
- Authentication: JWT

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.12+
- Docker and Docker Compose (optional, for containerized deployment)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/NarendraRavuri/ecommerce-microservices.git
cd ecommerce-microservices
```

2. **Set up virtual environment (optional)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies**

Navigate to each service directory and install the required Python packages.

```bash
pip install -r requirements.txt
```

### Running the Services

#### Without Docker

Navigate to each service directory and run the application.

```bash
flask run --port=5000  # For user_auth service
flask run --port=5001  # For product_management service
flask run --port=5002  # For order_processing service
```

#### With Docker Compose

To run all services together using Docker Compose:

```bash
docker-compose up --build
```

## Usage

The services can be accessed at the following URLs when running locally:

- User Authentication Service: `http://localhost:5001`
- Product Management Service: `http://localhost:5002`
- Order Processing Service: `http://localhost:5003`

## API Endpoints

### User Authentication Service

- **Register a User**
  - POST `/register`
  - Payload: `{"username": "testuser", "password": "password"}`

- **Log In**
  - POST `/login`
  - Payload: `{"username": "testuser", "password": "password"}`
  - Response: `{"access_token": "<JWT_Token>"}`

### Product Management Service

- **Create a Product** (Authenticated)
  - POST `/products`
  - Headers: `Authorization: Bearer <JWT_Token>`
  - Payload: `{"name": "New Product", "description": "Product Description", "price": 99.99, "quantity": 100}`

- **Get All Products** (Authenticated)
  - GET `/products`

- **Get a Single Product** (Authenticated)
  - GET `/products/<product_id>`

- **Update a Product** (Authenticated)
  - PUT `/products/<product_id>`
  - Headers: `Authorization: Bearer <JWT_Token>`
  - Payload: `{"name": "Updated Product", "description": "Updated Description", "price": 89.99, "quantity": 150}`

- **Delete a Product** (Authenticated)
  - DELETE `/products/<product_id>`
  - Headers: `Authorization: Bearer <JWT_Token>`

### Order Processing Service

- **Place an Order** (Authenticated)
  - POST `/orders`
  - Headers: `Authorization: Bearer <JWT_Token>`
  - Payload: `{"product_id": 1, "quantity": 2}`

- **Get User Orders** (Authenticated)
  - GET `/orders`
  - Headers: `Authorization: Bearer <JWT_Token>`

### Example Requests

1. **Register a User**

POST `http://localhost:5001/register`

Payload:

```json
{
    "username": "testuser",
    "password": "password"
}
```

2. **Log In**

POST `http://localhost:5001/login`

Payload:

```json
{
    "username": "testuser",
    "password": "password"
}
```

3. **Create a Product** (as an authenticated user)

POST `http://localhost:5002/products`

Headers:

```
Authorization: Bearer <JWT_Token>
```

Payload:

```json
{
    "name": "New Product",
    "description": "Product Description",
    "price": 99.99,
    "quantity": 100
}
```

4. **Place an Order** (as an authenticated user)

POST `http://localhost:5003/orders`

Headers:

```
Authorization: Bearer <JWT_Token>
```

Payload:

```json
{
    "product_id": 1,
    "quantity": 2
}
```

## Testing

To run unit tests for each service:

```bash
python -m unittest discover tests
```

## Authors

- **Narendra Ravuri** - [GitHub](https://github.com/NarendraRavuri/)
---

## DevOps and Source Control Management

This project uses Git and GitHub for source code
management and version control.

### Branching Strategy

The following branches are maintained:

- main: Contains stable application code.
- develop: Used for integrating development changes.
- feature/user-service: Used for User Service changes.
- feature/product-service: Used for Product Service changes.
- feature/order-service: Used for Order Service changes.

### Commit and Pull Request Workflow

1. Developers create feature branches from develop.
2. Changes are made and committed using Git.
3. Feature branches are pushed to GitHub.
4. Pull requests are created to merge changes into develop.
5. Changes are reviewed before merging.

### Jenkins Integration

GitHub is integrated with Jenkins using webhooks.
Whenever code changes are pushed to the configured
branch, Jenkins is triggered to execute the pipeline.

### Security Practices

- Sensitive credentials are not committed to GitHub.
- Private keys and environment files are excluded
  using .gitignore.
- Jenkins Credentials are used to manage secrets.