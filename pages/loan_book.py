from library.dal.loans import Loan

def loan_book():
    customer_id = int(input("Enter customer ID: "))
    book_id = int(input("Enter book ID: "))
    loan_date = input("Enter loan date (YYYY-MM-DD): ")
    loan = Loan('library.db')
    loan.add_loan(customer_id, book_id, loan_date)
    print("Book loaned successfully.")
