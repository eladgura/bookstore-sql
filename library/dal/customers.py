import sqlite3

class Customer:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT NOT NULL,
            age INTEGER NOT NULL
        )
        ''')
        self.conn.commit()

    def add_customer(self, name, city, age):
        cursor = self.conn.cursor()
        cursor.execute('''
        INSERT INTO customers (name, city, age)
        VALUES (?, ?, ?)
        ''', (name, city, age))
        self.conn.commit()

    def get_customer(self, customer_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM customers WHERE id = ?', (customer_id,))
        return cursor.fetchone()

    def get_all_customers(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM customers')
        return cursor.fetchall()

    def search_customer_by_name(self, name):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM customers WHERE name LIKE ?', ('%' + name + '%',))
        return cursor.fetchall()

    def remove_customer(self, customer_id):
        if not customer_id:
            raise ValueError("Customer ID is required.")
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM customers WHERE id = ?', (customer_id,))
        self.conn.commit()
