import sqlite3

class Book:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def add_book(self, name, author, year_published, book_type):
        if not name or not author or not year_published or not book_type:
            raise ValueError("Name, author, year_published, and book_type are required fields.")
        self.cursor.execute("INSERT INTO books (name, author, year_published, type) VALUES (?, ?, ?, ?)",
                            (name, author, year_published, book_type))
        self.conn.commit()

    def remove_book(self, book_id):
        if not book_id:
            raise ValueError("Book ID is required.")
        self.cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        self.conn.commit()

    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def search_book_by_name(self, name):
        self.cursor.execute("SELECT * FROM books WHERE name LIKE ?", ('%' + name + '%',))
        return self.cursor.fetchall()
