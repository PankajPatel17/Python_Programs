import tkinter as tk
from tkinter import messagebox
from product_management import ProductManager, Customer


def product_manager_login():
    def login():
        username = entry_username.get()
        password = entry_password.get()
        pm = ProductManager(username, password)
       
        messagebox.showinfo("Login", "Login successful!")
        window.quit() 

    window = tk.Tk()
    window.title("Product Manager Login")
    window.geometry("300x300")

    
    tk.Label(window, text="Username").pack()
    entry_username = tk.Entry(window)
    entry_username.pack()

    tk.Label(window, text="Password").pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    tk.Button(window, text="Login", command=login).pack()
    
    window.mainloop()

def customer_login():
    def login():
        username = entry_username.get()
        password = entry_password.get()
        customer = Customer(username, password)
        
        messagebox.showinfo("Login", "Login successful!")
        window.quit()  

    window = tk.Tk()
    window.title("Customer Login")
    window.geometry("300x300")
    
    tk.Label(window, text="Username").pack()
    entry_username = tk.Entry(window)
    entry_username.pack()

    tk.Label(window, text="Password").pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    tk.Button(window, text="Login", command=login).pack()

    window.mainloop()


def main():
    def open_product_manager():
        product_manager_login()

    def open_customer():
        customer_login()

    window = tk.Tk()
    window.title("Product Management System")
    window.geometry("300x300")
    
    tk.Button(window, text="Product Manager Login", command=open_product_manager).pack()
    tk.Button(window, text="Customer Login", command=open_customer).pack()
    
    window.mainloop()

if __name__ == "__main__":
    main()