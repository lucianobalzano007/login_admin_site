from pymongo import MongoClient
from os import getenv

def get_mongo_client():
    host_mongo = getenv('MONGO_HOST_NAME')
    user_mongo = getenv('MONGO_INITDB_ROOT_USERNAME')
    password_mongo = getenv('MONGO_INITDB_ROOT_PASSWORD')
    connection_string = f"mongodb://{user_mongo}:{password_mongo}@{host_mongo}:27017/"
    client = MongoClient(connection_string)
    return client

def crea_utente(new_user):
    client = get_mongo_client()
    db = client['studio_medico']
    collection = db['utenti'] 
    collection.insert_one(new_user)

def trova_utente(email):
    client = get_mongo_client()
    db = client['studio_medico']
    collection = db['utenti']  
    user = collection.find_one({"email": email})
    return user

def conta_utenti():
    client = get_mongo_client()
    db = client['studio_medico']
    collection = db['utenti'] 
    count = collection.count_documents({})
    return count