from pymongo import MongoClient

def get_mongo_client():
    # Sostituisci con la tua stringa di connessione MongoDB
    connection_string = "mongodb://example:example@mongo_med_app:27017/"
    client = MongoClient(connection_string)
    return client

def crea_utente(new_user):
    client = get_mongo_client()
    db = client['studio_medico']  # Sostituisci con il nome del tuo database
    collection = db['utenti']  # Sostituisci con il nome della tua collezione
    collection.insert_one(new_user)

def trova_utente(email):
    client = get_mongo_client()
    db = client['studio_medico']  # Sostituisci con il nome del tuo database
    collection = db['utenti']  # Sostituisci con il nome della tua collezione
    user = collection.find_one({"email": email})
    return user

def conta_utenti():
    client = get_mongo_client()
    db = client['studio_medico']  # Sostituisci con il nome del tuo database
    collection = db['utenti']  # Sostituisci con il nome della tua collezione
    count = collection.count_documents({})
    return count