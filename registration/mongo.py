
from pymongo import MongoClient

# Define MongoDB connection details directly here
MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DB_NAME = 'register_db'

def get_mongo_client():
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB_NAME]
    return client, db
