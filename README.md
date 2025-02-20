# 🚀 Django Project Setup Guide

## 📌 Prerequisites
Before you start, make sure you have the following installed:
- Python 3.6+
- Virtualenv (optional but recommended)

---

## 🛠️ Setup Instructions

### 1️⃣ Create a Virtual Environment
To keep dependencies isolated, create and activate a virtual environment:

```bash
python -m venv venv
```

- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```
- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```

---

### 2️⃣ Install Dependencies
Once inside the virtual environment, install the required packages:

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Apply Migrations
Run database migrations to set up the schema:

```bash
python manage.py migrate
```

If you need a superuser for the Django admin panel, create one:

```bash
python manage.py createsuperuser
```

---

### 4️⃣ Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
```

By default, the server runs at:

📍 **http://127.0.0.1:8000/**

---

## 📜 API Documentation
You can access the API documentation at:

🔗 **Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)  
🔗 **ReDoc UI (if enabled):** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

