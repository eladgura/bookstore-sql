import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dal.books import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book(':memory:')  # Use in-memory database for testing
        self.book.create_table()
        self.book.add_book('Test Book', 'Test Author', 2020, 1)

    def test_add_book(self):
        book = self.book.get_book(1)
        self.assertIsNotNone(book)
        self.assertEqual(book[1], 'Test Book')

if __name__ == '__main__':
    unittest.main()
