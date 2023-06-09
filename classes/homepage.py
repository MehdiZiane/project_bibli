import tkinter
import json
from tkinter import messagebox
from classes.class_book import Book
from classes.user_db import UserDatabase
from classes.book_db import BookDatabase
from classes.window import Window
from classes.book_details_page import BookDetailsPage
from classes.user_and_admin_page import UserPage
from classes.user_and_admin_page import AdminPage


class Homepage(Window):
    """Class use for display the homepage of your library app

    Args:
        Window : class to homepage inherit
    """

    def __init__(self):
        super().__init__()
        self.books = []
        self.user_db = UserDatabase()
        self.book_db = BookDatabase()
        self.book_details_page = None
        self.logged_in_user = None
        self.run_display()

    def run_display(self):
        self.display_book()
        self.display_login_signup()
        self.logged_in_user = None

    def display_book(self):
        self.frame_titre = tkinter.Frame(self.window)
        self.frame_titre.pack(side="top", padx=20, pady=20)
        titre = tkinter.Label(
            self.frame_titre, text="Welcome in the library", font=("Arial", 24)
        )
        titre.pack(pady=20)

        # Creating the left frame for displaying books
        self.frame_left = tkinter.Frame(self.window)
        self.frame_left.pack(side="left", padx=20, pady=20)

        # Loading books from a JSON file
        self.data = self.book_db.load_books()

        # Loop over books and display them
        for book in self.data:
            button_text = f"{book.title} - {book.author}"
            button = tkinter.Button(
                self.frame_left,
                text=button_text,
                command=lambda book=book: self.open_book_detail_page(book),
            )
            button.pack(pady=5)

        # Label which will receive information after the user logs in
        self.user_label = tkinter.Label(self.window, text="", font=("Arial", 16))
        self.user_label.pack(pady=10)

    def open_book_detail_page(self, book):
        """Function used to open a page giving details of a book

        Args:
            book : class to homepage inherit
        """

        self.frame_right.destroy()
        self.frame_left.destroy()
        self.frame_titre.destroy()
        self.book_details_page = BookDetailsPage(
            self.window, book, self.run_display, self.logged_in_user
        )

        self.book_details_page.run_display_book()

    def display_login_signup(self):
        """Function that displays the library login and registration buttons"""

        self.frame_right = tkinter.Frame(self.window)
        self.frame_right.pack(side="right", padx=20, pady=20)

        # Button Log In
        log_in_button = tkinter.Button(
            self.frame_right, text="Log In", command=self.login
        )
        log_in_button.pack(pady=10)

        # Button Sign Up
        sign_up_button = tkinter.Button(
            self.frame_right, text="Sign Up", command=self.create_account_dialog
        )
        sign_up_button.pack(pady=10)

        stop_button = tkinter.Button(
            self.frame_right, text="stop", command=self.stop_app
        )
        stop_button.pack(pady=10)

    def create_account(self, name, surname, email, password, dialog):
        """Function that allows the user to enter the data needed to create an account in the library.

        Args:
            nom (char): the name the user will choose
            prenom (char): the first name that the user will choose
            email (char): the email address that the user will choose
            password (char): the password that the user will choose
            dialog : the message displayed to the user
        """
        self.user_db.create_account(name, surname, email, password)
        messagebox.showinfo("Success", "Account created successfully!")
        dialog.destroy()

    def create_account_dialog(self):
        """Function that displays the dialog box where the user can enter him details to create a user account."""
        dialog = tkinter.Toplevel()
        dialog.title("Create Account")

        nom_label = tkinter.Label(dialog, text="Name:")
        nom_label.pack()
        nom_entry = tkinter.Entry(dialog)
        nom_entry.pack()

        prenom_label = tkinter.Label(dialog, text="Surname:")
        prenom_label.pack()
        prenom_entry = tkinter.Entry(dialog)
        prenom_entry.pack()

        email_label = tkinter.Label(dialog, text="Email:")
        email_label.pack()
        email_entry = tkinter.Entry(dialog)
        email_entry.pack()

        password_label = tkinter.Label(dialog, text="Password:")
        password_label.pack()
        password_entry = tkinter.Entry(dialog, show="*")
        password_entry.pack()

        create_button = tkinter.Button(
            dialog,
            text="Create Account",
            command=lambda: self.create_account(
                nom_entry.get(),
                prenom_entry.get(),
                email_entry.get(),
                password_entry.get(),
                dialog,
            ),
        )
        create_button.pack(pady=10)

    def login(self):
        """Function enablling the user to connect to his user account in the library"""
        dialog = tkinter.Toplevel()
        dialog.title("Log In")

        email_label = tkinter.Label(dialog, text="Email:")
        email_label.pack()
        email_entry = tkinter.Entry(dialog)
        email_entry.pack()

        password_label = tkinter.Label(dialog, text="Password:")
        password_label.pack()
        password_entry = tkinter.Entry(dialog, show="*")
        password_entry.pack()

        login_button = tkinter.Button(
            dialog,
            text="Log In",
            command=lambda: self.check_login(
                email_entry.get(), password_entry.get(), dialog
            ),
        )
        login_button.pack(pady=10)

    def check_login(self, email, password, dialog):
        """Function that checks the information the user has entered for their connection

        Args:
            email (char): the email address used by thr user
            password (char): the password used by the user
            dialog : the message displayed to the user
        """

        # Use the UserDatabase class to check authentication
        user = self.user_db.authenticate_user(email, password)
        if user:
            if not user["admin"]:
                print(user["admin"])
                messagebox.showinfo("Success", "Login successful!")
                # self.user_label.config(text=f"Welcome, {user['prenom']} {user['nom']}")  # Update the label with the user's details
                self.logged_in_user = (
                    user  # Update the logged_in_user variable in BookDetailsPage
                )
                self.frame_right.destroy()
                self.frame_left.destroy()
                self.frame_titre.destroy()
                UserPage(
                    self.window, self.logged_in_user, self.run_display
                ).display_user_page()

            else:
                messagebox.showinfo("succes", "welcome admin")
                self.logged_in_user = user
                self.frame_right.destroy()
                self.frame_left.destroy()
                self.frame_titre.destroy()
                AdminPage(
                    self.window, self.logged_in_user, self.run_display
                ).display_user_page()

        else:
            messagebox.showerror("Error", "Invalid email or password.")

        dialog.destroy()
