# Employee Management API

A RESTful API for managing employee records, built using **FastAPI, PostgreSQL, and SQLAlchemy's asynchronous ORM**. This project demonstrates CRUD operations, request validation, database integration, and REST API development.

## Features

- Create a new employee
- Retrieve all employees
- Retrieve an employee by ID
- Update employee details
- Delete an employee
- Validate request data using Pydantic
- Perform asynchronous database operations
- Handle duplicate email addresses and missing employee records
- Interactive API documentation using Swagger UI
- Automatically create database tables when the application starts

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy (Async)
- **Database Driver:** asyncpg
- **Validation:** Pydantic
- **Email Validation:** email-validator
- **Server:** Uvicorn
- **Environment Variables:** python-dotenv

## Project Structure

```text
Employee_Management_Apis/
├── app/
│   ├── crud/
│   │   ├── __init__.py
│   │   └── employee.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── employee.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── employees.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── employee.py
│   ├── database.py
│   └── main.py
├── requirements.txt
├── .env
└── README.md
```

### Folder Explanation

- **crud/** — Contains database operations such as creating, retrieving, updating, and deleting employees.
- **models/** — Defines SQLAlchemy database models.
- **routers/** — Defines API endpoints for employee management.
- **schemas/** — Defines Pydantic schemas for request validation and response serialization.
- **database.py** — Configures the database engine, sessions, and database connection.
- **main.py** — Initializes the FastAPI application.
- **requirements.txt** — Lists the required Python packages.
- **.env** — Stores environment variables and database configuration.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vamshi9381/Employee_Management_Apis.git
cd Employee_Management_Apis
```

### 2. Create a Virtual Environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Create the PostgreSQL Database

Open PostgreSQL or pgAdmin and create a database:

```sql
CREATE DATABASE employee_management;
```

Make sure PostgreSQL is running and that your database user has the required permissions.

### 5. Configure Environment Variables

Create a `.env` file in the root directory of the project.

Add your database connection URL:

```env
DATABASE_URL=postgresql+asyncpg://YOUR_USERNAME:YOUR_PASSWORD@localhost:5432/employee_management
```

Replace `YOUR_USERNAME` and `YOUR_PASSWORD` with your PostgreSQL credentials.

**Security:** Never upload your actual database password or other secrets to GitHub. Add `.env` to `.gitignore`.

### 6. Run the Application

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The application will normally run at:

`http://127.0.0.1:8000`

## API Documentation

Once the server is running, use the following URLs to explore and test the API.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc
- **Root endpoint:** http://127.0.0.1:8000/

## API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/employees/` | Create an employee |
| GET | `/employees/` | Retrieve all employees |
| GET | `/employees/{employee_id}` | Retrieve an employee by ID |
| PATCH | `/employees/{employee_id}` | Update selected employee fields |
| DELETE | `/employees/{employee_id}` | Delete an employee |

## Example API Requests

### 1. Create an Employee

**Method:** `POST`

**Endpoint:** `/employees/`

**Request Body:**

```json
{
  "name": "Ravi Kumar",
  "email": "ravi.kumar@example.com",
  "department": "Engineering",
  "salary": 55000
}
```

Example response:

```json
{
  "id": 1,
  "name": "Ravi Kumar",
  "email": "ravi.kumar@example.com",
  "department": "Engineering",
  "salary": 55000.0,
  "is_active": true
}
```

### 2. Retrieve All Employees

**Method:** `GET`

**Endpoint:**

```http
GET /employees/
```

Returns the employee records available in the database.

### 3. Retrieve an Employee by ID

**Method:** `GET`

**Endpoint:**

```http
GET /employees/1
```

Replace `1` with the required employee ID.

### 4. Update an Employee

**Method:** `PATCH`

**Endpoint:**

```http
PATCH /employees/1
```

**Request Body:**

```json
{
  "department": "Platform Engineering",
  "salary": 62000
}
```

Only the provided fields are updated.

### 5. Delete an Employee

**Method:** `DELETE`

**Endpoint:**

```http
DELETE /employees/1
```

A successful deletion returns `204 No Content`, with no response body.

## Testing with Postman

1. Start the FastAPI application.
2. Open Postman and create a new HTTP request.
3. Select the required HTTP method.
4. Enter the endpoint URL, such as `http://127.0.0.1:8000/employees/`.
5. For POST and PATCH requests, select **Body → raw → JSON**.
6. Enter the JSON request body.
7. Click **Send** and verify the response and HTTP status code.

You can also test the endpoints directly using Swagger UI at `/docs`.

## Error Handling

Common HTTP status codes include:

- **200 OK** — The request was successful.
- **201 Created** — An employee was created successfully.
- **204 No Content** — An employee was deleted successfully.
- **404 Not Found** — The requested employee does not exist.
- **409 Conflict** — An employee with the same email address already exists.
- **422 Unprocessable Entity** — Request validation failed.

The exact status codes depend on the endpoint implementation.

## Application Architecture

```text
        Client Application
       (Postman / Swagger UI)
                 |
                 v
          FastAPI Router
                 |
                 v
        Pydantic Validation
                 |
                 v
          CRUD Operations
                 |
                 v
       SQLAlchemy AsyncSession
                 |
                 v
          asyncpg Driver
                 |
                 v
             PostgreSQL
```

### How It Works

1. The client sends an HTTP request.
2. FastAPI routes the request to the appropriate endpoint.
3. Pydantic validates the incoming request data.
4. The CRUD layer performs the required database operation.
5. SQLAlchemy manages asynchronous database sessions.
6. The asyncpg driver communicates with PostgreSQL.
7. FastAPI returns the result as a JSON response when applicable.

## Future Improvements

- JWT-based authentication
- Role-based authorization
- Pagination and filtering
- Automated unit and integration tests
- Alembic database migrations
- Logging and monitoring
- Deployment to a cloud hosting platform

## Security Notes

- Store sensitive configuration in environment variables.
- Never commit database passwords or secret keys.
- Use authentication and authorization before exposing employee data in production.
- Configure production database credentials separately from development credentials.

## Author

**Vamshi Goud**

- GitHub: [vamshi9381](https://github.com/vamshi9381)
- Project: [Employee Management APIs](https://github.com/vamshi9381/Employee_Management_Apis)

## License

No license is currently specified. Add a LICENSE file if you intend to distribute this project publicly.
