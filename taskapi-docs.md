
# 📘 Task Management API Documentation

A simple RESTful API built with FastAPI for managing tasks per user with JWT-based authentication.

---

## 🔐 Authentication

This API uses **JWT Bearer Tokens** for authentication.

After login, include the token in the `Authorization` header like this:

```
Authorization: Bearer <your_token_here>
```

---

## 📁 Endpoints

---

### 1. 🚀 Register User

**POST** `/register/`

Register a new user.

#### Request Body

```json
{
  "username": "yourusername",
  "password": "yourpassword"
}
```

#### Responses

- `201 Created` – Successfully registered
- `400 Bad Request` – Username already exists

---

### 2. 🔐 Login

**POST** `/login/`

Authenticate and receive a JWT access token.

#### Request Body (Form data)

```x-www-form-urlencoded
username=yourusername
password=yourpassword
```

#### Response

```json
{
  "access_token": "jwt-token",
  "token_type": "bearer"
}
```

---

### 3. 📋 Get All Tasks

**GET** `/tasks/`

Returns a list of tasks belonging to the authenticated user.

#### Headers

```
Authorization: Bearer <token>
```

#### Response

```json
[
  {
    "id": 1,
    "title": "Buy milk",
    "description": "2 liters",
    "status": "TODO",
    "created_at": "2025-06-01T10:12:00",
    "updated_at": "2025-06-01T10:12:00",
    "owner_id": 1
  }
]
```

---

### 4. ➕ Create Task

**POST** `/tasks/`

Creates a new task.

#### Headers

```
Authorization: Bearer <token>
```

#### Request Body

```json
{
  "title": "Write report",
  "description": "Due Monday",
  "status": "IN_PROGRESS"
}
```

#### Response

```json
{
  "id": 2,
  "title": "Write report",
  "description": "Due Monday",
  "status": "IN_PROGRESS",
  "created_at": "2025-06-01T11:00:00",
  "updated_at": "2025-06-01T11:00:00",
  "owner_id": 1
}
```

---

### 5. 🔍 Get Task by ID

**GET** `/tasks/{id}/`

Retrieve a single task by its ID (must belong to authenticated user).

#### Response

```json
{
  "id": 2,
  "title": "Write report",
  "description": "Due Monday",
  "status": "IN_PROGRESS",
  "created_at": "2025-06-01T11:00:00",
  "updated_at": "2025-06-01T11:00:00",
  "owner_id": 1
}
```

---

### 6. ✏️ Update Task

**PUT** `/tasks/{id}/`

Update a task's details.

#### Request Body

```json
{
  "title": "Write summary report",
  "description": "Submit before 5 PM",
  "status": "DONE"
}
```

#### Response

Updated task object (same as above).

---

### 7. 🗑️ Delete Task

**DELETE** `/tasks/{id}/`

Delete a task by ID.

#### Response

```json
{"detail": "Task deleted"}
```

---

## 📌 Task Schema

| Field        | Type     | Description                            |
|--------------|----------|----------------------------------------|
| id           | int      | Unique task ID                         |
| title        | string   | Title of the task                      |
| description  | string   | Optional description                   |
| status       | enum     | One of: `TODO`, `IN_PROGRESS`, `DONE` |
| created_at   | datetime | Time of creation                       |
| updated_at   | datetime | Last update time                       |
| owner_id     | int      | ID of the user who owns the task       |

---

## 🔴 Error Handling

| Code | Reason                     |
|------|----------------------------|
| 400  | Invalid input              |
| 401  | Unauthorized (no token)    |
| 403  | Forbidden (not your task)  |
| 404  | Task not found             |
| 422  | Validation error           |

---

## 📚 Swagger UI

Interactive API documentation available at:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Testing the API

Use **Postman** or `curl`:

```bash
curl -X POST http://127.0.0.1:8000/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "1234"}'
```

Or explore all routes via Swagger UI.

---

## 🧠 Notes

- All `/tasks/` routes require valid JWT token
- Each user can only access their own tasks
