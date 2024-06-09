from library.dal.customers import Customer

def add_customer():
    name = input("Enter customer name: ")
    city = input("Enter city: ")
    age = int(input("Enter age: "))
    customer = Customer('library.db')
    customer.add_customer(name, city, age)
    print("Customer added successfully.")
