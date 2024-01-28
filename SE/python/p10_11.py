'''
Create a login application using Tkinter and SQLite
'''
from tkinter import *
import sqlite3

with sqlite3.connect("details.db") as db:
    cursor = db.cursor()
    
cursor.execute(""" CREATE TABLE IF NOT EXISTS users(username text PRIMARY KEY, password text NOT NULL); """)

def add_new_user():
	newuser=username.get()
	newpass= password.get()
	
	cursor.execute("SELECT COUNT(*) FROM users WHERE username='"+newuser+"'")
	result = cursor.fetchone()
	
	if int(result[0])>0:
		error["text"] = "Error: User already exists"
	else:
		error["text"] = "Added new user"
		cursor.execute("INSERT INTO users(username, password) VALUES(?,?)",(newuser, newpass))
		db.commit()
		
window =Tk()
window.geometry("450x180")

error = Message(text="", width=160)
error.place(x=30, y=10)

label1 = Label(text = "Enter Username:")
label1.place(x = 30, y = 40)

username = Entry(text = "")
username.place(x=150, y=40, width=200, height= 25)

label1 = Label(text = "Enter Password:")
label1.place(x = 30, y = 80)

password = Entry(text = "", show="*")
password.place(x=150, y=80, width=200, height= 25)

button = Button(text="Add", command= add_new_user)
button.place(x=150, y=120, width=75, height= 35)
window.mainloop()