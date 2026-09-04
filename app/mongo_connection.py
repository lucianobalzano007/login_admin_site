from pymongo import MongoClient

def get_mongo_client():
    connection_string = "mongodb://example:example@mongo_med_patente:27017/"
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