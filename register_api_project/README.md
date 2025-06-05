# Register API Project

This project is a Django-based REST API for user registration and authentication, connected to MongoDB.

## 🚀 Features

- User Registration
- User Login
- Token-Based Authentication
- MongoDB Integration using `pymongo`
- Environment-based configuration (`.env` support)
- REST API tested with Django REST Framework (DRF) browser

## 🛠️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- MongoDB
- pymongo
- dotenv

## 📁 Project Structure


## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/AnkitSinghinnovontek/ankit.git
   cd register_api
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
pip install -r requirements.txt
CURRENT_ENVIRONMENT=development
LOCAL_MONGO_URI=mongodb://localhost:27017
python manage.py runserver
POST /register/ – Register a new user
POST /login/ – Login and get auth token