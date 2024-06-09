from library.dal.customers import Customer

def find_customer_by_name():
    name = input("Enter customer name to search: ")
    customer = Customer('library.db')
    found_customers = customer.search_customer_by_name(name)
    if not found_customers:
        print("No customers found with that name.")
    else:
        print("Customers found:")
        for found_customer in found_customers:
            print(found_customer)
