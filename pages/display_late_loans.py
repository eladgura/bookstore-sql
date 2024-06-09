from library.dal.loans import Loan

def display_late_loans():
    loan = Loan('library.db')
    late_loans = loan.get_late_loans()
    if not late_loans:
        print("No late loans found.")
    else:
        for late_loan in late_loans:
            print(late_loan)
