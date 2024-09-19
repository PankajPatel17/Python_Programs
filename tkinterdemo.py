from tkinter import *
import mysql.connector
import tkinter.messagebox as msg


def create_conn():
    return mysql.connector.connect(
        host = 'locslhost',
        user = 'root',
        password = "",
        database = 'mydb'
    )
def insert_db():
    if e_fname.get()=="" or e_lname.get()=="" or e_mail.get()=="" or e_mobile.get()=="":
        msg.showinfo("insert status","all fields are mendatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()

