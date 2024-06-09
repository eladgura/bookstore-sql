from library.dal.books import Book

def find_book_by_name():
    name = input("Enter book name to search: ")
    book = Book('library.db')
    found_books = book.search_book_by_name(name)
    if not found_books:
        print("No books found with that name.")
    else:
        print("Books found:")
        for found_book in found_books:
            print(found_book)
