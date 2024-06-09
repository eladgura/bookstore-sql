from library.dal.books import Book

def add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    year_published = int(input("Enter year of publication: "))
    book_type = int(input("Enter book type (1, 2, or 3): "))
    book = Book('library.db')
    book.add_book(name, author, year_published, book_type)
    print("Book added successfully.")
