<div align="center">

# 🔐 Authentication Project: Backend

### A secure Token Authentication API built with Django REST Framework

**Python • Django • Django REST Framework • Token Authentication**

</div>

---

## 📖 About The Project

This is the **backend** of a full-stack authentication system. It exposes a clean REST API that lets users **register**, **log in to receive an auth token**, and access **protected data** that is available only to authenticated users.

The API is consumed by a React frontend: 👉 [Authentication-Frontend](https://github.com/MuhammadAhsan1-rgb/Authentication-Frontend)

---

## ✨ Features

- 📝 **User Registration**: create a new account through the API
- 🔑 **Token-Based Login**: receive a unique token on successful login
- 🛡️ **Protected Endpoint**: the Details API is accessible only with a valid token
- 🚫 **Clean Error Responses**: requests without a valid token get a proper `401 Unauthorized`
- 🔌 **Frontend Ready**: built to work with a React client

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core language |
| **Django** | Web framework |
| **Django REST Framework** | Building the REST API |
| **DRF Token Authentication** | Securing endpoints |

---

## 🔄 How Authentication Works

```
1. Register  →  POST user details        →  Account created
2. Login     →  POST credentials         →  Token returned
3. Request   →  Header: Authorization: Token <your_token>
4. Access    →  Valid token  →  200 OK
                No token     →  401 Unauthorized
```

---

## 📡 API Endpoints

> Paths below are examples. Adjust them to match your `urls.py`.

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `POST` | `/api/register/` | Register a new user | ❌ No |
| `POST` | `/api/login/` | Log in and get a token | ❌ No |
| `GET` | `/api/details/` | Get protected user details | ✅ Yes |

### Example: Calling the Protected Endpoint

```bash
curl -H "Authorization: Token <your_token>" http://127.0.0.1:8000/api/details/
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/MuhammadAhsan1-rgb/Authentication-Project.git
cd Authentication-Project

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
```

The API will be available at **http://127.0.0.1:8000/**

---

## 🔗 Related Repository

| Part | Repository |
|---|---|
| 🎨 Frontend (React + Tailwind CSS) | [Authentication-Frontend](https://github.com/MuhammadAhsan1-rgb/Authentication-Frontend) |

---

## 💡 What I Learned

- Implementing the complete **Token Authentication** flow in DRF
- Protecting API endpoints with permission classes
- Connecting a React frontend to a Django REST API
- Handling authenticated requests using token headers

---

## 👨‍💻 Author

**Muhammad Ahsan**
GitHub: [@MuhammadAhsan1-rgb](https://github.com/MuhammadAhsan1-rgb)

---

<div align="center">

⭐ If you found this project helpful, consider giving it a star!

</div>
