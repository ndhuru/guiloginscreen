Last login: Mon Oct 16 07:48:42 on console
pl252491@7118L20 ~ % vim tkinterguiproject.py






















import tkinter as tk
import sqlite3
import hashlib

conn = sqlite3.connect('allmyusers.db')
cursor = conn.cursor()

newtableQuery = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT
);
'''
cursor.execute(newtableQuery)


def newUser(username, password, first_name, last_name):
    insertQuery = '''
    INSERT INTO users (username, password, first_name, last_name)
    VALUES (?, ?, ?, ?);

