from library.dal.customers import Customer
from pages.display_page import display_page


def display_all_customers():
    customer = Customer('library.db')
    customers = customer.get_all_customers()
    if not customers:
        print("No customers found.")
    else:
        page_size = 5  # Number of items per page
        page_number = 1
        while True:
            display_page(customers, page_size, page_number)
            choice = input("Press Enter to view next page or 'q' to return to menu: ")
            if choice.lower() == 'q':
                break
            page_number += 1
