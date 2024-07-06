from models import Checkout
from storage import Storage
import logging

# Configure logging
logging.basicConfig(filename='library.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')
class CheckoutManager:
    """Manages checkout operations."""

    def __init__(self):
        self.storage = Storage()

    def checkout_book(self):
        """Checks out a book after validating user ID and ISBN."""
        user_id = input("Enter user ID: ")
        isbn = input("Enter ISBN of the book to checkout: ")

        user = self.storage.get_user_by_id(user_id)
        if not user:
            print(f"Invalid User ID ({user_id}). Checkout failed.")
            return

        book = self.storage.get_book_by_isbn(isbn)
        if not book:
            print(f"Invalid ISBN ({isbn}). Checkout failed.")
            return

        if not book.available:
            print(f"Book with ISBN ({isbn}) is already checked out. Checkout failed.")
            return

        checkout = Checkout(user_id, isbn)
        self.storage.add_checkout(checkout)

        book.available = False
        self.storage.update_book(book)
        logging.info(f"Book with ISBN ({isbn}) checked out by user {user_id}.")
        print(f"Book with ISBN ({isbn}) checked out successfully by user {user_id}.")
            
    def checkin_book(self):
        """Checks in a book using its ISBN."""
        isbn = input("Enter the ISBN of the book to check in: ")
        book = self.storage.get_book_by_isbn(isbn)

        if not book:
            print(f"No book found with ISBN {isbn}. Check-in failed.")
            return

        if book.available:
            print(f"Book with ISBN {isbn} is already checked in.")
            return

        self.storage.return_book(isbn)

        book.available = True
        self.storage.update_book(book)
        logging.info(f"Book with ISBN {isbn} checked in successfully.")
        print(f"Book with ISBN {isbn} checked in successfully.")