import sys
import os
from library.dal.customers import Customer
from library.dal.books import Book
from library.dal.loans import Loan
from pages.display_page import display_page
from pages.add_book import add_book
from pages.add_customer import add_customer
from pages.loan_book import loan_book
from pages.return_book import return_book
from pages.display_all_books import display_all_books
from pages.display_all_customers import display_all_customers
from pages.display_all_loans import display_all_loans
from pages.display_late_loans import display_late_loans
from pages.find_book_by_name import find_book_by_name
from pages.find_customer_by_name import find_customer_by_name
from pages.remove_book import remove_book
from pages.remove_customer import remove_customer
from database_setup import initialize_db

# Function to display the main menu
def display_menu():
    print("\nLibrary Management System")
    print("1. Exit")
    print("2. Add a new customer")
    print("3. Add a new book")
    print("4. Loan a book")
    print("5. Return a book")
    print("6. Display all books")
    print("7. Display all customers")
    print("8. Display all loans")
    print("9. Display late loans")
    print("10. Find book by name")
    print("11. Find customer by name")
    print("12. Remove book")
    print("13. Remove customer")

# Main function to run the library management system
def main():
    clear_terminal()
    db_name = 'library.db'
    initialize_db(db_name)  # Initialize the database
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            print("Exiting program.")
            sys.exit()
        elif choice == '2':
            add_customer()
        elif choice == '3':
            add_book()
        elif choice == '4':
            loan_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            display_all_books()
        elif choice == '7':
            display_all_customers()
        elif choice == '8':
            display_all_loans()
        elif choice == '9':
            display_late_loans()
        elif choice == '10':
            find_book_by_name()
        elif choice == '11':
            find_customer_by_name()
        elif choice == '12':
            remove_book()
        elif choice == '13':
            remove_customer()
        else:
            print("Invalid choice. Please try again.")

# Function to clear the terminal screen
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
