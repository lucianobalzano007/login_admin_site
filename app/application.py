from flask import Flask, render_template, request, redirect, url_for, session, g, flash
from user import User
import mongo_connection

app = Flask(__name__)
app.secret_key = b'8a665c57fc268229c8fa04aab499193063bd6b93eff981a361ad634e360ae755'  # Cambia questa chiave in una chiave reale

@app.route('/')
def index():
    if 'email' in session:
        user = User.get_user_by_email(session['email'])
        if user.get_role() == 'Admin':
            return redirect(url_for('home_admin'))
    if mongo_connection.conta_utenti() == 0:
        return redirect(url_for('register_admin'))
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
            if user.get_role() == 'Admin':
                return redirect(url_for('home_admin'))
        flash("Errore 401: Email e/o password non valide", "error")
        return redirect(url_for('login'))
    return render_template('login.html')
    
@app.route('/home_admin')
def home_admin():
    utente=User.get_user_by_email(session['email'])
    print(utente.get_cf())
    return render_template('index_admin.html',utente=utente)

@app.route('/register_admin', methods=['POST', 'GET'])
def register_admin():
    if request.method == 'POST' and mongo_connection.conta_utenti() == 0:
        name = request.form['name']
        surname = request.form['surname']
        birthdate = request.form['birth']
        cf = request.form['cf']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        role = 'Admin'
        print(f"Name: {name}, Surname: {surname}, Birthdate: {birthdate}")  # Debugging line
        print(f"Email: {email}, Password: {password}")  # Debugging line
        if password != confirm_password:
            flash("Errore 400: Le password non coincidono", "error")
            return redirect(url_for('register_user'))
        if mongo_connection.trova_utente(email)!= None:
            flash("Errore 400: Email già in uso", "error")
            return redirect(url_for('register_user'))
        user = User(name, surname, birthdate, cf, email, password, role)
        user.create_user()
        return redirect(url_for('login'))
    elif mongo_connection.conta_utenti()!=0:
        return redirect(url_for('login'))
    return render_template('register_admin.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
