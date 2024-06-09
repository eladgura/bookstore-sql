# Library Management System

This Library Management System is a command-line interface (CLI) application designed to manage books, customers, and loans in a library. The system allows for adding, viewing, searching, and removing books and customers, as well as managing loans and returns of books.

## Table of Contents

- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Database Initialization](#database-initialization)
- [Running the Application](#running-the-application)
- [Menu Options](#menu-options)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Add New Customer**: Add new customers to the library database.
- **Add New Book**: Add new books to the library database.
- **Loan a Book**: Loan a book to a customer and record the loan details.
- **Return a Book**: Return a loaned book and update the loan record.
- **Display All Books**: Display a list of all books in the library.
- **Display All Customers**: Display a list of all customers registered in the library.
- **Display All Loans**: Display a list of all book loans.
- **Display Late Loans**: Display a list of loans that are overdue.
- **Find Book by Name**: Search for a book by its name.
- **Find Customer by Name**: Search for a customer by their name.
- **Remove Book**: Remove a book from the library database.
- **Remove Customer**: Remove a customer from the library database.

## Setup and Installation

1. **Clone the Repository**


git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
Create and Activate a Virtual Environment


Copy code
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
Install Dependencies


Copy code
pip install -r requirements.txt
Usage
Initialize the Database

Before running the application for the first time, initialize the database:


Copy code
python database_setup.py
Run the Application


Copy code
python library_client.py
Follow the On-Screen Menu

The main menu will prompt you with various options to manage your library.

Project Structure
markdown
Copy code
library-management-system/
│
├── library/
│   ├── dal/
│   │   ├── books.py
│   │   ├── customers.py
│   │   └── loans.py
│   └── __init__.py
│
├── pages/
│   ├── add_book.py
│   ├── add_customer.py
│   ├── display_all_books.py
│   ├── display_all_customers.py
│   ├── display_all_loans.py
│   ├── display_late_loans.py
│   ├── display_page.py
│   ├── find_book_by_name.py
│   ├── find_customer_by_name.py
│   ├── loan_book.py
│   ├── remove_book.py
│   ├── remove_customer.py
│   └── return_book.py
│
├── database_setup.py
├── library_client.py
└── requirements.txt
Database Initialization
The database_setup.py script is responsible for creating the necessary tables in the SQLite database. This script ensures the database is set up correctly each time the application starts.

Database Tables
Books Table: Stores information about books, including the book ID, name, author, year published, and type.
Customers Table: Stores customer information, including the customer ID, name, city, and age.
Loans Table: Stores loan information, including the loan ID, customer ID, book ID, loan date, and return date.
Running the Application
To start the application, run the library_client.py script. You will be presented with a menu that allows you to choose various actions, such as adding a book or customer, loaning a book, and more.

Menu Options
Exit: Exit the program.
Add a new customer: Add a new customer to the database.
Add a new book: Add a new book to the database.
Loan a book: Loan a book to a customer.
Return a book: Return a loaned book.
Display all books: Display a list of all books.
Display all customers: Display a list of all customers.
Display all loans: Display a list of all loans.
Display late loans: Display a list of late loans.
Find book by name: Search for a book by name.
Find customer by name: Search for a customer by name.
Remove book: Remove a book from the database.
Remove customer: Remove a customer from the database.
Example Usage
Adding a Book: Select option 2 from the menu and follow the prompts to enter the book's details.
Loaning a Book: Select option 3 and enter the required details to loan a book to a customer.
Returning a Book: Select option 4 and provide the loan ID and return date to return a book.
Finding a Book by Name: Select option 9 and enter the book name to search for it.

Contributing
Contributions are welcome! Please open an issue or submit a pull request with any changes or suggestions.