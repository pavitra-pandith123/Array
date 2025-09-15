from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load data
with open('data/medicines.json') as f:
    medicines = json.load(f)

with open('data/users.json') as f:
    users = json.load(f)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('chatbot'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    medicine_info = None
    if request.method == 'POST':
        medicine_name = request.form['medicine_name']
        medicine_info = medicines.get(medicine_name)
    return render_template('chatbot.html', medicine_info=medicine_info)

if __name__ == '__main__':
    app.run(debug=True)