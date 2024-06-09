from library.dal.loans import Loan

def return_book():
    loan_id = int(input("Enter loan ID: "))
    return_date = input("Enter return date (YYYY-MM-DD): ")
    loan = Loan('library.db')
    loan.return_book(loan_id, return_date)
    print("Book returned successfully.")
