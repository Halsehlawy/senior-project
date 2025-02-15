import sqlite3
import hashlib
connection=sqlite3.connect('admin.db')
cursor=connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS admin(
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")
username,password="admin",hashlib.sha256("admin".encode('utf-8')).hexdigest()
cursor.execute("INSERT INTO admin(username,password)VALUES(?,?)",(username,password))
connection.commit()

