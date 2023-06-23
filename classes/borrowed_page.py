import tkinter
import json
from tkinter import messagebox
from classes.user_db import UserDatabase
from classes.book_db import BookDatabase


class Borrowed_page:
    """Class used to display a page showing books borrowed or reserved"""

    def __init__(self, window, callback):
        self.window = window
        self.callback = callback
        self.user_db = UserDatabase()
        self.book_db = BookDatabase()

    def run_display_borrowed(self):
        """Function for displaying borrowed books in the graphical interface"""
        self.frame_borrowed_left = tkinter.Frame(self.window)
        self.frame_borrowed_left.pack(side="left", padx=20, pady=20)

        self.frame_borrowed_right = tkinter.Frame(self.window)
        self.frame_borrowed_right.pack(side="right", padx=20, pady=20)

        self.frame_borrowed_top = tkinter.Frame(self.window)
        self.frame_borrowed_top.pack(side="top", padx=20, pady=20)

        self.display_borrowed()

    def display_borrowed(self):
        # Load the books from the database
        data = self.book_db.load_books()

        # Filter the books to display only the reserved ones
        reserved_books = [book for book in data if book.is_reserved]

        return_button = tkinter.Button(
            self.frame_borrowed_right,
            text="Return",
            command=self.back_page,
        )
        return_button.pack(pady=5)

        if not reserved_books:
            # Display a message if there are no reserved books
            no_books_label = tkinter.Label(
                self.frame_borrowed_top,
                text="No books are currently borrowed.",
                font=("Arial", 16),
            )
            no_books_label.pack(pady=10)
        else:
            # Display the borrowed books
            for book in reserved_books:
                user = self.user_db.get_user_by_id(book.reserved_by)
                print(user)

                if user:
                    reserved_by_info = f"reserved by: {user['name']} {user['surname']}"
                else:
                    reserved_by_info = "reserved by: Unknown User"

                book_info = (
                    f"Title: {book.title}\nAuthor: {book.author}\n{reserved_by_info}"
                )

                book_bouton = tkinter.Button(
                    self.frame_borrowed_left,
                    text=book_info,
                    font=("arial", 12),
                    justify="left",
                    command=lambda book_id=book.book_id: self.show_confirmation_dialog(
                        book_id
                    ),
                )
                book_bouton.pack(pady=5)

    def show_confirmation_dialog(self, book_id):
        """Function that opens a booking confirmation dialogue box

        Args:
            book_id : Book id to be confirmed
        """
        # Display a dialogue box with "Yes" and "No" buttons
        result = messagebox.askyesno(
            "Confirmation", "will you accept the borrow of this book "
        )

        # Check the user's answer
        if result == True:  # If the user has selected on "Yes".
            self.accept_borrow(book_id)
        else:  # If the user has selected on "No
            self.deny_borrow(book_id)

    def accept_borrow(self, book_id):
        """Function enabling admin to accept a loan

        Args:
            book_id : Book id to be accepted
        """
        # Load book data from the database
        with open("./db/book.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        # Search for a book by ID
        book = next((book for book in data if book["id"] == book_id), None)

        # Check if the book has been found
        if book:
            # Updating book information
            book["is_borrowed"] = True
            book["borrowed_by"] = book["reserved_by"]
            book["is_reserved"] = False

            # Save changes in the database
            with open("./db/book.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            # Display a success message
            messagebox.showinfo("Success", "Book borrow accepted.")
        else:
            # Display an error message if the book is not found
            messagebox.showerror("Error", "Book not found.")

    def deny_borrow(self, book_id):
        """Function allowing admin to refuse a loan

        Args:
            book_id : Book id to be refused
        """
        # Load book data from the database
        with open("./db/book.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        # Search for a book by ID
        book = next((book for book in data if book["id"] == book_id), None)

        # Check if the book has been found
        if book:
            # Reset book reservation information
            book["is_reserved"] = False
            book["reserved_by"] = None

            # Save changes in the database
            with open("./db/book.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            # Display a success message
            messagebox.showinfo("Success", "Book borrow denied.")
        else:
            # Display an error message if the book is not found
            messagebox.showerror("Error", "Book not found.")

    def back_page(self):
        """Function to return to the previous page"""
        self.frame_borrowed_left.destroy()
        self.frame_borrowed_right.destroy()
        self.frame_borrowed_top.destroy()
        self.callback()
