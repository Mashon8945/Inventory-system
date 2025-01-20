# Inventory-system

# Inventory Management System

This is a simple backend system built with Python, Django, and MySQL to manage an inventory of products. The system allows you to list, add, update, and delete products through a REST API.

---

## Features

- List all products in the inventory.
- Add new products with details such as name, description, price, and stock.
- Update the details of existing products.
- Delete products by their ID.


## Prerequisites

1. Python 3.8 or higher
2. MySQL Server
3. pip (Python package installer)

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone <https://github.com/Mashon8945/Inventory-system.git>
cd inventory_system
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the Database

1. Create a MySQL database named `inventory_system`.
2. Update the `DATABASES` section in `inventory_system/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'inventory_system',
           'USER': 'root',
           'PASSWORD': 'password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

---

## API Endpoints

### 1. List All Products
**URL:** `/api/products/`

**Method:** `GET`

**Response:**
```json
[
  {
    "id": 1,
    "name": "Bread",
    "description": "Description of Bread",
    "price": "65.00",
    "stock": 100,
    "created_at": "2025-01-01T12:00:00",
    "updated_at": "2025-01-02T12:00:00"
  }

  {
    "id": 2,
    "name": "Sugar",
    "description": "1KG of Sugar",
    "price": "250.00",
    "stock": 50,
    "created_at": "2025-01-01T12:00:00",
    "updated_at": "2025-01-02T12:00:00"
  }
]
```

### 2. Add a New Product
**URL:** `/api/products/add/`

**Method:** `POST`

**Request Body:**
```json
  {
    "name": "Bread",
    "description": "Description of Bread",
    "price": "65.00",
    "stock": 100
  }
```

**Response:**
```json
{
  "id": 1,
  "message": "Product added successfully"
}
```

### 3. Update a Product
**URL:** `/api/products/update/<product_id>/`

**Method:** `PUT`

**Request Body:**
```json
{
  "name": "Bread",
  "price": 67.00
}
```

**Response:**
```json
{
  "message": "Product updated successfully"
}
```

### 4. Delete a Product
**URL:** `/api/products/delete/<product_id>/`

**Method:** `DELETE`

**Response:**
```json
{
  "message": "Product deleted successfully"
}
```

---

## Testing

Use a tool like **Postman** to test the API endpoints.

Example with `curl`:

- **List Products:**
  ```bash
    GET http://127.0.0.1:8000/api/products/
  ```

- **Add Product:**
  ```bash
    POST -H "Content-Type: application/json" \
       -d '{"name": "Product A", "description": "Test product", "price": 20.50, "stock": 50}' \
       http://127.0.0.1:8000/api/products/add/
  ```

- **Update Product:**
  ```bash
    PUT -H "Content-Type: application/json" \
       -d '{"price": 30.00}' \
       http://127.0.0.1:8000/api/products/update/1/
  ```

- **Delete Product:**
  ```bash
    DELETE http://127.0.0.1:8000/api/products/delete/1/
  ```


