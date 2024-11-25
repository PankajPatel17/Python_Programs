from db_connection import get_db_connection

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        pass  
class ProductManager(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def register(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO product_managers (username, password) VALUES (%s, %s)", (self.username, self.password))
        connection.commit()
        cursor.close()
        connection.close()


class Customer(User):
    def __init__(self, username, password, balance=0.0):
        super().__init__(username, password)
        self.balance = balance

    def register(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO customers (username, password, balance) VALUES (%s, %s, %s)", (self.username, self.password, self.balance))
        connection.commit()
        cursor.close()
        connection.close()

