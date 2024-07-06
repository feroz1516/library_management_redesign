class Book:
    """Represents a book in the library."""

    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return (
            f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, "
            f"Available: {self.available}"
        )


class User:
    """Represents a library user."""

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"Name: {self.name}, User ID: {self.user_id}"


class Checkout:
    """Represents a book checkout."""

    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn

    def __str__(self):
        return f"User ID: {self.user_id}, ISBN: {self.isbn}"