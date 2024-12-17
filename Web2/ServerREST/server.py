from flask import Flask, render_template, request
import psycopg2
from psycopg2 import sql

# configurazione della conesssione al DB
DB_CONFIG = {'host': 'localhost',
             'port': '5432',
             'dbname': 'Accademia',
             'user': 'postgres',
             'password': 'postgres'
}

# Func per settare dbname
def set_dbname(new_name):
    DB_CONFIG['dbname'] = new_name
    return DB_CONFIG


# Func per ottenere la connessione al database
def db_connect():
    conn = psycopg2.connect(
        dbname = DB_CONFIG['dbname'], 
        user = DB_CONFIG['user'],
        password = DB_CONFIG['password'],
        host = DB_CONFIG['host'],
    )
    return conn


# Query the database and obtain data as Python objects
def get_query(query):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(sql.SQL(query))
    res = cur.fetchall()
    return res


# TEST
print(get_query('SELECT * FROM Persona;'))


