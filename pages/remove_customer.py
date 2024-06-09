from library.dal.customers import Customer

def remove_customer():
    customer_id = int(input("Enter customer ID to remove: "))
    customer = Customer('library.db')
    customer.remove_customer(customer_id)
    print("Customer removed successfully.")
