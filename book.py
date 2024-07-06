from models import Book
from storage import Storage
import logging

# Configure logging
logging.basicConfig(filename='library.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')

class BookManager:
    """Manages book-related operations."""

    def __init__(self):
        self.storage = Storage()

    def add_book(self):
        """Adds a new book after validating input."""
        while True:
            title = input("Enter title: ")
            author = input("Enter author: ")

            #ISBN is usually 13 or 10 digit number but for the sake of simplicity the constrains were not added
            isbn = input("Enter ISBN: ")
            if title and author and isbn:
                break
            else:
                print("Title, Author, and ISBN cannot be empty. Please try again.")

        book = Book(title, author, isbn)
        self.storage.add_book(book)
        logging.info(f"New book added: {book}") # Log book addition
        print("Book added successfully!")

    def list_books(self):
        """Lists all books."""
        books = self.storage.get_books()
        if books:
            for book in books:
                print(book)
        else:
            print("No books found.")
            
    def search_books(self):
        """Searches for books based on title, author, or ISBN."""
        search_by = input(
            "Search by (1) title, (2) author, or (3) ISBN? Enter the corresponding number: "
        )

        if search_by == "1":
            search_query = input("Enter the title to search for: ")
            matching_books = [
                book for book in self.storage.get_books() if search_query.lower() in book.title.lower()
            ]

        elif search_by == "2":
            search_query = input("Enter the author to search for: ")
            matching_books = [
                book for book in self.storage.get_books() if search_query.lower() in book.author.lower()
            ]

        elif search_by == "3":
            search_query = input("Enter the ISBN to search for: ")
            matching_books = [
                book for book in self.storage.get_books() if search_query.lower() == book.isbn.lower()
            ]

        else:
            print("Invalid search option. Please try again.")
            return

        if matching_books:
            print("Found books:")
            for book in matching_books:
                print(book)
        else:
            print("No books found matching your search criteria.")

    def update_book(self):
        """Updates an existing book's information."""
        isbn = input("Enter the ISBN of the book you want to update: ")
        book = self.storage.get_book_by_isbn(isbn)

        if book:
            print(f"Current information for book with ISBN {isbn}: {book}")
            title = input("Enter new title (leave blank to keep current): ")
            author = input("Enter new author (leave blank to keep current): ")

            if not title:
                title = book.title  # Keep the current title
            if not author:
                author = book.author  # Keep the current author

            book = Book(title, author, isbn)
            self.storage.update_book(book)
            logging.info(f"Book with ISBN {isbn} updated in successfully.")
            print("Book updated successfully!")
        else:
            print(f"No book found with ISBN {isbn}")

    def delete_book(self):
        """Deletes a book by its ISBN."""
        isbn = input("Enter the ISBN of the book you want to delete: ")
        self.storage.delete_book(isbn)
        logging.info(f"Book with ISBN {isbn} deleted in successfully.")
        print(f"Book with ISBN {isbn} deleted successfully!")
        
    def check_book_availability(self):
        """Checks and displays the availability of a book by ISBN."""
        isbn = input("Enter the ISBN of the book to check availability: ")
        book = self.storage.get_book_by_isbn(isbn)

        if book:
            if book.available:
                print(f"The book '{book.title}' is currently available.")
            else:
                print(f"The book '{book.title}' is currently checked out.")
        else:
            print(f"No book found with ISBN {isbn}.")