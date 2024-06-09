import sqlite3

def create_books_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        author TEXT NOT NULL,
        year_published INTEGER NOT NULL,
        type INTEGER NOT NULL CHECK(type IN (1, 2, 3))
    )
    ''')
    conn.commit()

def create_customers_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')
    conn.commit()

def create_loans_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS loans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        custID INTEGER NOT NULL,
        bookID INTEGER NOT NULL,
        loanDate TEXT NOT NULL,
        returnDate TEXT,
        FOREIGN KEY (custID) REFERENCES customers (id),
        FOREIGN KEY (bookID) REFERENCES books (id)
    )
    ''')
    conn.commit()

def initialize_db(db_name):
    conn = sqlite3.connect(db_name)
    create_books_table(conn)
    create_customers_table(conn)
    create_loans_table(conn)
    conn.close()

if __name__ == '__main__':
    db_name = 'library.db'
    initialize_db(db_name)
    print(f"Database '{db_name}' initialized successfully.")
