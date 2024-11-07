import os

from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

def get_client(host=None, port=None, username=None, password=None):
    database_uri = "mongodb+srv://" if host and host not in ['localhost', '0.0.0.0', '127.0.0.1', 'mongodb', 'database'] else "mongodb://"
    if username and password:
        database_uri += f"{username}:{password}@"

    if host:
        database_uri += f"{host}"
    else:
        database_uri += f"localhost"
    
    if port:
        database_uri += f":{port}"
    
    client = MongoClient(database_uri)
    return client

def get_database(name, host=DATABASE_HOST, port=DATABASE_PORT, username=DATABASE_USERNAME, password=DATABASE_PASSWORD):
    client = get_client(host, port, username, password)
    database = client[name]
    return database

def get_collection(collection_name, database_name=DATABASE_NAME):
    database = get_database(database_name)
    collection = database[collection_name]
    return collection