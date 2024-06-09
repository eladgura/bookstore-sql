from library.dal.loans import Loan
from pages.display_page import display_page

def display_all_loans():
    loan = Loan('library.db')
    loans = loan.get_all_loans()
    if not loans:
        print("No loans found.")
    else:
        page_size = 5  # Number of items per page
        page_number = 1
        while True:
            display_page(loans, page_size, page_number)
            choice = input("Press Enter to view next page or 'q' to return to menu: ")
            if choice.lower() == 'q':
                break
            page_number += 1
