# 🛡️ drf-secure-api-jwt-encrypt-cicd-limitation

A fully-featured Django Rest Framework (DRF) project implementing **JWT authentication**, **AES field-level encryption**, **API rate limiting**, and **CI/CD integration via GitHub Actions**. Designed to demonstrate secure API development with access control, token-based authentication, encrypted data storage, request throttling, and automated testing — ideal for production-grade systems.


Designed to demonstrate how to build secure, production-ready REST APIs with token-based access, encrypted data storage, request throttling, and automated testing pipelines.

---

## 📌 Features

- ✅ JWT Authentication (with `djangorestframework-simplejwt`)
- 🔐 AES Field-Level Encryption using `cryptography`
- ⏳ API Rate Limiting (User Throttle: 5 requests/minute)
- 📮 Secure API Endpoints with DRF `ListCreateAPIView`
- 🔄 CI/CD Pipeline with **GitHub Actions**
- 🧪 Basic Unit Test for Secure Data POST API
- 🧱 Minimal & Modular Project Structure

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Django 5.x**
- **Django REST Framework**
- **SimpleJWT** for token auth
- **Cryptography** for encryption
- **GitHub Actions** for automated testing

---

## 📁 Project Structure

drf-secure-api-jwt-encrypt-cicd-limitation/
├── api/
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── urls.py
│ └── views.py
├── secure_api_project/
│ ├── settings.py
│ ├── urls.py
├── .github/
│ └── workflows/
│ └── django.yml
├── manage.py
├── requirements.txt
└── README.md



---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Ainy07/drf-secure-api-jwt-encrypt-cicd-limitation.git
cd drf-secure-api-jwt-encrypt-cicd-limitation
```

### 2. Create & Activate Virtual Environment
```bash

python -m venv env
source env/bin/activate      # On Linux/Mac
env\Scripts\activate         # On Windows
```


### 3. Install Dependencies
```bash

pip install -r requirements.txt
```

### 4. Run Migrations
```bash

python manage.py makemigrations
python manage.py migrate
```


### 5. Create Superuser
```bash

python manage.py createsuperuser
```


### 6. Run Server
```bash

python manage.py runserver
``` 


## 🔐 API Authentication Flow
### 🔸 1. Obtain Token
## POST /api/token/

```json

{
  "username": "yourusername",
  "password": "yourpassword"
}
```

# Response:

```json

{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}

```

### 🔸 2. Access Secure Endpoint
## POST /api/secure-data/

Headers:

```makefile

Authorization: Bearer <access_token>

```

## Body:

```json

{
  "plain_text": "My secret info"
}
```

## Response:

```json

{
  "id": 1,
  "decrypted_text": "My secret info"
}
```

### ✅ Running Tests
## To run the API tests:

```bash

python manage.py test api
```

### 🚀 CI/CD with GitHub Actions
The project includes a GitHub Actions workflow that:

Installs dependencies

Runs tests automatically on every push to main

.github/workflows/django.yml:

```yaml

name: Django CI

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          cd secure_api_project
          python manage.py test api
```

          
### 🔒 Security Notes
Encryption key is randomly generated per session for demo purposes. In production, use a secure static key, loaded from .env or a vault.

JWT settings like expiration can be tuned via SIMPLE_JWT in settings.py.

### 📄 License
This project is open-source and free to use under the MIT License.

### 💡 Credits
Django & DRF Official Docs

cryptography Python Library

simplejwt JWT package




