import crypto
import mongo_connection

class User:
    def __init__(self, name, surname, birthdate, cf, email, password, role):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.cf = cf
        self.email = email
        self.password = password
        self.role = role
    
    def create_user(self):
        new_password = crypto.hash_password(self.password)
        new_user = {
            "name": self.name,
            "surname": self.surname,
            "birthdate": self.birthdate,
            "cf" : self.cf,
            "email": self.email,
            "role" : self.role,
            "password": new_password
        }
        mongo_connection.crea_utente(new_user)
    
    def get_user_by_email(email):
        user = mongo_connection.trova_utente(email)
        if user is None:
            return None
        utente = User(user['name'], user['surname'], user['birthdate'], user['cf'], user['email'], user['password'], user['role'])
        return utente
    
    def get_lista_utenti(lista_mongo):
        lista_utenti=[]
        for user in lista_mongo:
            utente = User(user['name'], user['surname'], user['birthdate'], user['cf'], user['email'], user['password'], user['role'])
            lista_utenti.append(utente)
        return lista_utenti
    
    def check_password(self, password):
        # Qui puoi aggiungere la logica per verificare la password dell'utente
        hashed_password = crypto.hash_password(password)
        if self.password == hashed_password:
            return True
        else:
            return False
    
    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def get_birtdate(self):
        return self.birthdate
    
    def get_cf(self):
        return self.cf
    
    def get_role(self):
        return self.role