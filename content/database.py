"""
database = 'sqlite'
if database == 'mysql':
    import mysql.connector as sql
    conn = sql.connect(user='root',database='data')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTO_INCREMENT, username TEXT, password TEXT, date TEXT, time TEXT, access INTEGER)")
elif database == 'sqlite':
    import sqlite3 as sql
    conn = sql.connect(database='data.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, password TEXT, date TEXT, time TEXT, access INTEGER)")
"""
import sqlite3 as sql
import random
import time

conn = sql.connect(database='../data.db')
cursor = conn.cursor()

datenow, timenow = time.strftime('%d/%m/%y'), time.strftime('%H:%M')

def load_database():
    """Cria as tabelas do banco de dados e cria um usuario/senha admin/admin para poder entrar no programa inicialmente"""
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, date TEXT, time TEXT, access INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS value(id INTEGER PRIMARY KEY AUTOINCREMENT, value REAL, info TEXT, date TEXT, time TEXT)")
    cursor.execute("SELECT * FROM users WHERE username = 'remember'")
    result = cursor.fetchone()
    if result is None:
        cursor.execute("INSERT INTO users(username,password,date,time,access) VALUES('remember','',?,?,5)", (datenow, timenow))
        conn.commit()

    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    result = cursor.fetchone()
    if result is None:
        cursor.execute("INSERT INTO users(username,password,date,time,access) VALUES('admin','admin',?,?,5)", (datenow, timenow,))
        conn.commit()

def fill_database(initial=0,final=50):
    """Preenche a tabela com dados para testar no programa"""
    for i in range(initial,final):
        data = [random.randint(0, 2000) + 1, 'N/A', time.strftime('%d/%m/%Y'), time.strftime('%H:%M')]
        cursor.execute("INSERT INTO 'value'(value,info,date,time) VALUES(?,?,?,?)", data)
    conn.commit()

if __name__ == '__main__':
    load_database()
    fill_database(0,200)
