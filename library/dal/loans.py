import sqlite3
class Loan:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
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
        self.conn.commit()

    def add_loan(self, cust_id, book_id, loan_date):
        cursor = self.conn.cursor()
        cursor.execute('''
        INSERT INTO loans (custID, bookID, loanDate)
        VALUES (?, ?, ?)
        ''', (cust_id, book_id, loan_date))
        self.conn.commit()

    def get_loan(self, loan_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM loans WHERE id = ?', (loan_id,))
        return cursor.fetchone()

    def get_all_loans(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM loans')
        return cursor.fetchall()

    def get_late_loans(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM loans WHERE returnDate IS NULL AND date(loanDate, "+10 days") < date("now")')
        return cursor.fetchall()

    def return_book(self, loan_id, return_date):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE loans SET returnDate = ? WHERE id = ?', (return_date, loan_id))
        self.conn.commit()
        print("Book returned successfully.")
