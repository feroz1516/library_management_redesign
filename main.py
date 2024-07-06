from book import BookManager
from user import UserManager
from check import CheckoutManager


def main_menu():
    """Displays the main menu and returns the user's choice."""
    print("\nLibrary Management System")
    print("1. Manage Books")
    print("2. Manage Users")
    print("3. Checkout/Check-in Books")
    print("4. Exit")
    choice = input("Enter choice: ")
    return choice


def book_menu(book_manager):
    """Displays the book management menu and handles user input."""
    while True:
        print("\nBook Management Menu:")
        print("1. Add Book")
        print("2. List Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Books")
        print("6. Check Book Availability") 
        print("7. Back to Main Menu") 
        choice = input("Enter choice: ")
        # using if-elif-else blocks because 'match' supports python version greater than 3.10

        if choice == "1":
            book_manager.add_book()
        elif choice == "2":
            book_manager.list_books()
        elif choice == "3":
            book_manager.update_book()
        elif choice == "4":
            book_manager.delete_book()
        elif choice == "5":
            book_manager.search_books()
        elif choice == "6":
            book_manager.check_book_availability() 
        elif choice == "7":  
            break
        else:
            print("Invalid choice. Please try again.")


def user_menu(user_manager):
    """Displays the user management menu and handles user input."""
    while True:
        print("\nUser Management Menu:")
        print("1. Add User")
        print("2. List Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            user_manager.add_user()
        elif choice == "2":
            user_manager.list_users()
        elif choice == "3":
            user_manager.update_user()
        elif choice == "4":
            user_manager.delete_user()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


def checkout_menu(checkout_manager):
    """Displays the checkout management menu and handles user input."""
    while True:
        print("\nCheckout/Check-in Menu:")
        print("1. Checkout Book")
        print("2. Check-in Book")
        print("3. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            checkout_manager.checkout_book()
        elif choice == "2":
            checkout_manager.checkin_book()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    """Initializes managers and runs the main application loop."""
    book_manager = BookManager()
    user_manager = UserManager()
    checkout_manager = CheckoutManager()

    while True:
        choice = main_menu()

        if choice == "1":
            book_menu(book_manager)
        elif choice == "2":
            user_menu(user_manager)
        elif choice == "3":
            checkout_menu(checkout_manager)
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()