from flask import Flask, render_template, request, redirect, url_for, session, g

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia questa chiave in una chiave reale

# Un dizionario temporaneo per memorizzare gli utenti (usa un database in un'app reale)
utenti = {}

@app.route('/')
def to_login():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(f"Email: {email}, Password: {password}")  # Debugging line
        if email in utenti and utenti[email] == password:
            return redirect(url_for('home'))
        return "Credenziali non valide", 401
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
        print(f"Name: {name}, Surname: {surname}, Birthdate: {birthdate}")  # Debugging line
        print(f"Email: {email}, Password: {password}")  # Debugging line
        if email in utenti:
            return "Utente già esistente", 400
        utenti[email] = password
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
