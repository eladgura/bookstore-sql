from library.dal.books import Book

def remove_book():
    book_id = int(input("Enter book ID to remove: "))
    book = Book('library.db')
    book.remove_book(book_id)
    print("Book removed successfully.")
