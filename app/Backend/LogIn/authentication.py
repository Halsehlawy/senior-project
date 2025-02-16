import sqlite3
import hashlib
username=input("Enter username:")
password=input("Enter password:")
hashedPassword=hashlib.sha256(password.encode()).hexdigest()
connection=sqlite3.connect('admin.db')
cursor=connection.cursor()
cursor.execute("SELECT * FROM admin WHERE username =? AND password=?",(username,hashedPassword))
if cursor.fetchall():
    print("Login succeful")
else:
    print("Login failed")