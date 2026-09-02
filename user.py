import crypto
import mongo_connection

class User:
    def __init__(self, name, surname, birthdate, email, password):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.email = email
        self.password = password
    
    def create_user(self):
        # Qui puoi aggiungere la logica per salvare l'utente nel database
        new_password = crypto.hash_password(self.password)
        new_user = {
            "name": self.name,
            "surname": self.surname,
            "birthdate": self.birthdate,
            "email": self.email,
            "password": new_password
        }
        mongo_connection.crea_utente(new_user)
    
    def get_user_by_email(email):
        # Qui puoi aggiungere la logica per recuperare l'utente dal database
        user = mongo_connection.trova_utente(email)
        utente = User(user['name'], user['surname'], user['birthdate'], user['email'], user['password'])
        return utente
    
    def check_password(self, password):
        # Qui puoi aggiungere la logica per verificare la password dell'utente
        hashed_password = crypto.hash_password(password)
        if self.password == hashed_password:
            return True
        else:
            return False