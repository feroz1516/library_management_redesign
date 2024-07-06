import json
from models import Book, User, Checkout

class Storage:
    """Handles data storage and retrieval using JSON files."""

    def __init__(self, filename="library.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """Loads data from the JSON file."""
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"books": [], "users": [], "checkouts": []}

    def save_data(self):
        """Saves data to the JSON file."""
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def add_book(self, book):
        """Adds a new book to the storage."""
        self.data["books"].append(book.__dict__)
        self.save_data()

    def get_books(self):
        """Retrieves all books."""
        return [Book(**book_data) for book_data in self.data["books"]]

    def get_book_by_isbn(self, isbn):
        """Retrieves a book by its ISBN."""
        for book_data in self.data["books"]:
            if book_data["isbn"] == isbn:
                return Book(**book_data)
        return None
        
    def update_book(self, book):
        """Updates a book in the storage."""
        for i, book_data in enumerate(self.data["books"]):
            if book_data["isbn"] == book.isbn:
                self.data["books"][i] = book.__dict__
                self.save_data()
                return
    
    def delete_book(self, isbn):
        """Deletes a book from the storage."""
        self.data["books"] = [
            book_data for book_data in self.data["books"] if book_data["isbn"] != isbn
        ]
        self.save_data()

    def add_user(self, user):
        """Adds a new user to the storage."""
        self.data["users"].append(user.__dict__)
        self.save_data()

    def get_users(self):
        """Retrieves all users."""
        return [User(**user_data) for user_data in self.data["users"]]

    def get_user_by_id(self, user_id):
        """Retrieves a user by their ID."""
        for user_data in self.data["users"]:
            if user_data["user_id"] == user_id:
                return User(**user_data)
        return None
    
    def update_user(self, user):
        """Updates a user in the storage."""
        for i, user_data in enumerate(self.data["users"]):
            if user_data["user_id"] == user.user_id:
                self.data["users"][i] = user.__dict__
                self.save_data()
                return
    
    def delete_user(self, user_id):
        """Deletes a user from the storage."""
        self.data["users"] = [
            user_data for user_data in self.data["users"] if user_data["user_id"] != user_id
        ]
        self.save_data()

    def add_checkout(self, checkout):
        """Adds a new checkout to the storage."""
        self.data["checkouts"].append(checkout.__dict__)
        self.save_data()

    def get_checkouts(self):
        """Retrieves all checkouts."""
        return [Checkout(**checkout_data) for checkout_data in self.data["checkouts"]]

    def get_checkout_by_isbn(self, isbn):
        """Retrieves a checkout by ISBN."""
        for checkout_data in self.data["checkouts"]:
            if checkout_data["isbn"] == isbn:
                return Checkout(**checkout_data)
        return None

    def return_book(self, isbn):
        """Removes a checkout from the storage."""
        self.data["checkouts"] = [
            checkout_data for checkout_data in self.data["checkouts"] if checkout_data["isbn"] != isbn
        ]
        self.save_data()