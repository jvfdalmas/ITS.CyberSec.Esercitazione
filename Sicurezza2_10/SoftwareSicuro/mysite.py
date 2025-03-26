"""
per scoprire tutte le interfacce di rete della vostra macchina
ip a | grep inet

per impostare un IP nuovo
sudo ip a add 192.168.101.10/24 dev enp58s0u1u2

Per impostare mysql
    sudo apt install mysql-client
    mysql -h 127.0.0.1 -P 13306 -uroot -proot

    create database cyber05;
    use cyber05;

    CREATE TABLE users (
        id SERIAL,
        username VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL );
    CREATE TABLE items (
        id SERIAL,
        name VARCHAR(255) UNIQUE NOT NULL,
        description VARCHAR(255) NOT NULL );

    insert into items (name, description) values ("pixel9 pro", "latest high cost from google");
    insert into items (name, description) values ("pixel9", "latest low cost from google");

    importare pymysql e flask
    sudo apt install python3-pymysql
    sudo apt install python3-flask
    
"""

import os
import pymysql
from hashlib import sha256

from flask import Flask, request, g, redirect, url_for, render_template, session, flash

import re

def sanitize_username(username):
    """Sanitize username: allow only letters, numbers, underscores, and dots"""
    username = username.strip()  # Remove spaces
    if not re.match(r"^[a-zA-Z0-9_.]{3,20}$", username):
        raise ValueError("Invalid username: Use only letters, numbers, underscores, and dots (3-20 chars).")
    return username

def sanitize_password(password):
    """Sanitize password: allow only letters, numbers, and common special characters""" 
    password = password.strip()  # Remove spaces
    if not re.match(r"^[a-zA-Z0-9@#$%^&+=!]{8,20}$", password):
        raise ValueError("Invalid password: Use only letters, numbers, and common special characters (8-20 chars).")
    return password


SECRET_KEY = 'AAA'  # Replace with your own secret key.

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

def get_db():
    """
    Open a new database connection if there is none yet for the current application context.
    """
    if 'db' not in g:
        # Connect to MySQL, witouth autocommit and dbname
        g.db = pymysql.connect(
            host="127.0.0.1",
            user="root",
            port=13306,
            password="root",
            cursorclass=pymysql.cursors.DictCursor
        )
        g.cursor = g.db.cursor()
    return g.cursor, g.db

def get_db_nodatabase():
    """
    Open a new database connection if there is none yet for the current application context.
    """
    # Connect to MySQL, witouth autocommit and dbname
    g.db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        port=13306,
        password="root",
        cursorclass=pymysql.cursors.DictCursor
    )
    g.cursor = g.db.cursor()
    g.cursor.execute('''create database if not exists cyber;''')
    g.db.commit()
    g.cursor.close()
    g.db.close()

    # Connect to MySQL, with dbname
    g.db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        port=13306,
        password="root",
        database="cyber",
        cursorclass=pymysql.cursors.DictCursor
    )
    g.cursor = g.db.cursor()
    return g.cursor, g.db


@app.teardown_appcontext
def close_db(error):
    """
    Closes the database connection at the end of the request.
    """
    cursor = g.pop('cursor', None)
    if cursor is not None:
        cursor.close()
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """Create user table if it doesn't exist."""
    db, conn = get_db_nodatabase()
    db.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL,
        username VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL );
    ''')
    db.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id SERIAL,
        name VARCHAR(255) UNIQUE NOT NULL,
        description VARCHAR(255) NOT NULL );
    ''')
    conn.commit()
    try:
        db.execute('insert into users (username, password) values ("admin", "vivalaroma");')
    except:
        pass
    try:
        db.execute('insert into items (name, description) values ("pixel9 pro", "latest high cost from google");')
        db.execute('insert into items (name, description) values ("pixel9", "latest low cost from google");')
    except:
        pass
    conn.commit()

@app.before_request
def initialize():
    """Initialize the database before the first request."""
    init_db()
   
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if session.get('username') is None or session['username'] != "admin":
            flash("Only the administrator can register new users.", "error")
            return redirect(url_for('login'))

        username = request.form['username']
        password = request.form['password']
        db, conn = get_db()
        
        # Check if user already exists
        db.execute(f"SELECT * FROM users WHERE username = '{username}'")
        existing_user = db.fetchall()

        print("Sto per registrare")

        if existing_user:
            flash("Username already taken, please choose another.", "error")
            return redirect(url_for('register'))

        # Hash and store the new user’s password
        db.execute(
            f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
        conn.commit()
        print("registrato")

        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('login'))

    # GET request -> Show registration form
    return render_template('register.html')

@app.route('/fill', methods=['GET'])
def fill():
    howmany = 100000
    db, conn = get_db()
    for i in range(1, howmany):
        r = os.urandom(8)
        name = f"User {r.hex()}"
        password = f"Password {r.hex()}"
        db.execute(f"INSERT INTO users (username, password) VALUES ('{name}', '{password}')")
    conn.commit()
    flash(f"{howmany} items added!", "success")
    return redirect(url_for('getall'))

@app.route('/getall', methods=['GET'])
def getall():
    db, conn = get_db()
    db.execute("SELECT * FROM users")
    items = db.fetchall()

    return render_template('dynamicusers.html', items=items)


@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if 'user_id' not in session:
        flash("You must be logged in to add items.", "warning")
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        db, conn = get_db()
        db.execute(f"INSERT INTO items (name, description) VALUES ('{name}', '{description}')")
        conn.commit()
        flash("Item added!", "success")
        return redirect(url_for('show_items'))

    return render_template('base.html', content="""
    <form method="POST">
        <label for="name">Item Name:</label>
        <input type="text" name="name" required><br><br>
        <label for="description">Description:</label>
        <textarea name="description"></textarea><br><br>
        <button type="submit">Add Item</button>
    </form>
    """)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, conn = get_db()


        sql = f"SELECT * FROM users WHERE username='{username}' and password='{password}'"
    
        print(request.form)
        print(sql)
        db.execute(sql)
        user=db.fetchall()
        if user:
            user=user[0]

        # Validate user credentials
        if user: # and user['password']==password:
            # Store user info in session
            session['user_id'] = sha256(password.encode()).hexdigest()
            session['username'] = user["username"]
            
            flash("Login successful!", "success")
            return redirect(url_for('protected_page'))

        flash("Invalid credentials. Please try again.", "error")
        return redirect(url_for('login'))

    # GET request -> Show login form
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

@app.route('/protected')
def protected_page():
    if 'user_id' not in session:
        flash("You must be logged in to access this page.", "warning")
        return redirect(url_for('login'))

    return render_template('protected_page.html')

@app.route('/protected_static')
def protected_static():
    if 'user_id' not in session:
        flash("You must be logged in to view this page.", "warning")
        return redirect(url_for('login'))
    
    # Return the static content from a file (or a template) only if logged in
    return app.send_static_file('protected_page.html')

@app.route('/public')
def public_page():
    return render_template('free_public_page.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/MiaBanca.html')
def miabanca():
    return render_template('MiaBanca.html')

# La gestione dei dati applicativi
@app.route('/items')
def show_items():
    if 'user_id' not in session:
        flash("You must be logged in to view items.", "warning")
        return redirect(url_for('login'))

    db, conn = get_db()
    db.execute("SELECT * FROM items")
    items = db.fetchall()

    return render_template('dynamic.html', items=items)


myip = "127.0.0.1"
myport = 32001

if __name__ == '__main__':
    with app.app_context():
        init_db()  # Ensure the database is initialized
    app.run(host=myip, port=myport, debug=False)
