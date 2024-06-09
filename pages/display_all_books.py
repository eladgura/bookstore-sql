from library.dal.books import Book
from pages.display_page import display_page


def display_all_books():
    book = Book('library.db')
    books = book.get_all_books()
    if not books:
        print("No books found.")
    else:
        page_size = 5  # Number of items per page
        page_number = 1
        while True:
            display_page(books, page_size, page_number)
            choice = input("Press Enter to view next page or 'q' to return to menu: ")
            if choice.lower() == 'q':
                break
            page_number += 1
