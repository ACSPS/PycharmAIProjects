from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from datetime import datetime
import sqlite3
import requests


app = Flask(__name__)
app.secret_key = 'your_secret_key'

def init_db():  # a function to initialise the database and create the users table if it doesn't exist
    conn = sqlite3.connect('ai_flask.db')  # connects to the database named basic_flask.db
    cursor = conn.cursor()  # creates a cursor object to interact with the database using SQL commands
    #  cursor.execute() is used to execute SQL commands
    cursor.execute('''        
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')
    conn.commit() # commits the changes to the database
    conn.close()  # to closes the connection to the database

# Database connection
def get_db_connection():
    conn = sqlite3.connect('ai_flask.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']  # gets the username from the form
    password = request.form['password']  # gets the password from the form
    age = request.form['age']  # gets the age from the form
    conn = sqlite3.connect('ai_flask.db')  # connects to the database
    cursor = conn.cursor()  # creates a cursor object to interact with the database
    # inserts the user details into the users table
    cursor.execute('INSERT INTO users (username, password, age) VALUES (?, ?, ?)', (username, password, age))
    conn.commit()  # commits the changes to the database
    conn.close()  # closes the connection to the database
    flash('User registered successfully!', 'success')  # displays a success message to the user
    return redirect(url_for('login'))  # redirects the user to the login page


# login route
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('ai_flask.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?',(username,password))
    # is a placeholder for the values that will be passed in the execute() function
    # (username,password) are the values that will be passed in the execute() function
    # This is a parameterised query to prevent SQL injection attacks
    user = cursor.fetchone() # fetches the first row of the results
    conn.close()
    if user:
        session['user'] = user [1]
        print (user)
        session['age'] = user [3]
        return redirect(url_for('welcome'))
    return 'Login failed'

@app.route('/welcome')
def welcome():
    if 'user' in session:
        user = session['user']
        age = session['age']
        return render_template('welcome.html', user=user, age=age)
    return redirect(url_for('login'))


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user', None)
    session.pop('age', None)
    return redirect(url_for('login'))




@app.route('/api/chat', methods=['GET', 'POST'])  # Define the route for the chat page
def chat():
    if 'messages' not in session:
        session['messages'] = []  # starts an empty list for messages

    if request.method == 'POST':
        user_input = request.form['user_input']  # to get the user's input from the form
        session['messages'].append({'sender': 'You', 'text': user_input})  # saves the user's message

        return redirect(url_for('/api/chat'))  # Redirect to the chat page to update the messages
    return render_template('welcome.html', messages=session['messages'])



if __name__ == '__main__':
    app.run(debug=True)  # to run the app
