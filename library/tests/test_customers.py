import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dal.customers import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(':memory:')  # Use in-memory database for testing
        self.customer.create_table()
        self.customer.add_customer('Test Customer', 'Test City', 30)

    def test_add_customer(self):
        customer = self.customer.get_customer(1)
        self.assertIsNotNone(customer)
        self.assertEqual(customer[1], 'Test Customer')

if __name__ == '__main__':
    unittest.main()
