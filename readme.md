# 🚀 Network Route Optimization API

A **Django REST Framework based backend service** that models a network of nodes and edges and provides APIs to compute the **shortest path between nodes using Dijkstra's Algorithm**.

The system also stores and provides **route query history with filtering and pagination**.

---

# 🧰 Tech Stack

- Python 3.12
- Django
- Django REST Framework
- drf-yasg (Swagger Documentation)
- SQLite (default Django DB)

---

# 🏗 Project Architecture

The project follows a **layered architecture** to maintain separation of concerns.

```
View Layer → Service Layer → Repository Layer → Database
```

| Layer | Responsibility |
|------|------|
| Views | Handle HTTP requests and responses |
| Services | Business logic |
| Repositories | Database operations |
| Models | Database schema |

---

# 📁 Project Structure

```
network_optimizer/
│
├── routing/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   │
│   ├── views/
│   │   ├── node_views.py
│   │   ├── edge_views.py
│   │   └── route_views.py
│   │
│   ├── services/
│   │   ├── node_service.py
│   │   ├── edge_service.py
│   │   └── route_service.py
│   │
│   ├── repositories/
│   │   ├── node_repository.py
│   │   ├── edge_repository.py
│   │   └── route_repository.py
│   │
│   └── exceptions.py
│
├── common/
│   ├── exception_handler.py
│   └── pagination.py
│
└── manage.py
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone the Repository

```
git clone <repo_url>
cd network_optimizer
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate environment

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install django
pip install djangorestframework
pip install drf-yasg
```

---

## 4️⃣ Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

## 5️⃣ Run Server

```
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# 📚 API Documentation

Swagger UI is available at:

```
http://127.0.0.1:8000/swagger/
```

---

# 🚀 Future Improvements

Possible enhancements include:

- Caching frequently requested routes
- Graph database integration
- Authentication and authorization
- Rate limiting

---

# 👨‍💻 Author

Backend implementation using **Django REST Framework** for **Network Route Optimization Assignment**.