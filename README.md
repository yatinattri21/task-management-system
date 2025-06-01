# ✅ FastAPI Task Management API

A simple and clean RESTful API built with **FastAPI** that supports **user registration, JWT login**, and full **CRUD operations** for tasks, each linked to their respective user.

---

## 🔧 Features

- 🧾 User registration and secure JWT login
- 📋 Create, read, update, and delete your own tasks
- 🔐 Task access restricted to the authenticated user
- 🔍 Built-in interactive API docs at `/docs`
- ✅ Testing with `pytest`

---

## ⚙️ Tech Stack

- **FastAPI**
- **SQLite (via SQLAlchemy)**
- **JWT Authentication (with python-jose)**
- **Uvicorn (ASGI server)**
- **pytest** for unit testing

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/taskapi.git
cd taskapi
```

### 2. Create and activate virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI server
```bash
uvicorn main:app --reload
```

###4. Open browser and visit
```bash
http://127.0.0.1:8000/docs
```




