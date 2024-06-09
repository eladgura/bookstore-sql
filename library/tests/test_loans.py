import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dal.books import Book
from dal.customers import Customer
from dal.loans import Loan

class TestLoan(unittest.TestCase):
    def setUp(self):
        self.book = Book(':memory:')
        self.customer = Customer(':memory:')
        self.loan = Loan(':memory:')
        
        self.book.create_table()
        self.customer.create_table()
        self.loan.create_table()
        
        # Add test book and customer
        self.book.add_book('Test Book', 'Test Author', 2020, 1)
        self.customer.add_customer('Test Customer', 'Test City', 30)

    def test_add_loan(self):
        self.loan.add_loan(1, 1, '2024-06-07')
        loan = self.loan.get_loan(1)
        self.assertIsNotNone(loan)
        self.assertEqual(loan[1], 1)
        self.assertEqual(loan[2], 1)

if __name__ == '__main__':
    unittest.main()
