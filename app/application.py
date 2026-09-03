from flask import Flask, render_template, request, redirect, url_for, session, g, flash
from user import User
import mongo_connection

app = Flask(__name__)
app.secret_key = b'8a665c57fc268229c8fa04aab499193063bd6b93eff981a361ad634e360ae755'  # Cambia questa chiave in una chiave reale

@app.route('/')
def index():
    if 'email' in session:
        return redirect(url_for('home'))
    if mongo_connection.conta_utenti() == 0:
        return redirect(url_for('register_user'))
    return redirect(url_for('login'))

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(f"Email: {email}, Password: {password}")  # Debugging line
        user = User.get_user_by_email(email)
        if user == None:
            flash("Errore 401: Email e/o password non valide", "error")
            return redirect(url_for('login'))
        if user.check_password(password):
            session['email'] = email
            return redirect(url_for('home'))
        flash("Errore 401: Email e/o password non valide", "error")
        return redirect(url_for('login'))
    return render_template('login.html')
    
@app.route('/home')
def home():
    return render_template('index.html')

@app.get('/register')
def render_register_page():
    return render_template('register.html')

@app.route('/register', methods=['POST', 'GET'])
def register_user():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        birthdate = request.form['birth']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        print(f"Name: {name}, Surname: {surname}, Birthdate: {birthdate}")  # Debugging line
        print(f"Email: {email}, Password: {password}")  # Debugging line
        if password != confirm_password:
            flash("Errore 400: Le password non coincidono", "error")
            return redirect(url_for('register_user'))
        if mongo_connection.trova_utente(email)!= None:
            flash("Errore 400: Email già in uso", "error")
            return redirect(url_for('register_user'))
        user = User(name, surname, birthdate, email, password)
        user.create_user()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
