from models import User
from storage import Storage
import logging

# Configure logging
logging.basicConfig(filename='library.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')

class UserManager:
    """Manages user-related operations."""

    def __init__(self):
        self.storage = Storage()

    def add_user(self):
        """Adds a new user after validating input."""
        while True:
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")

            if name and user_id:
                break
            else:
                print("Name and User ID cannot be empty. Please try again.")

        user = User(name, user_id)
        self.storage.add_user(user)
        logging.info(f"New user added: {user}") # Log user addition
        print("User added successfully!")

    def list_users(self):
        """Lists all users."""
        users = self.storage.get_users()
        if users:
            for user in users:
                print(user)
        else:
            print("No users found.")
            
    def update_user(self):
        """Updates an existing user's information."""
        user_id = input("Enter the ID of the user you want to update: ")
        user = self.storage.get_user_by_id(user_id)

        if user:
            print(f"Current information for User ID {user_id}: {user}")
            name = input("Enter new name (leave blank to keep current): ")
            if not name:
                name = user.name  # Keep the current name

            user = User(name, user_id)
            self.storage.update_user(user)
            logging.info(f"User updated: {user}") # Log user addition

            print("User updated successfully!")
        else:
            print(f"No user found with User ID {user_id}")
    
    def delete_user(self):
        """Deletes a user by their ID."""
        user_id = input("Enter the ID of the user you want to delete: ")
        user = self.storage.get_user_by_id(user_id)
        self.storage.delete_user(user_id)
        logging.info(f"User Deleted: {user}") # Log user addition

        print(f"User with ID {user_id} deleted successfully!")