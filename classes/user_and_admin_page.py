import tkinter
import json
from tkinter import messagebox
from classes.class_book import Book
from classes.user_db import UserDatabase
from classes.class_user import User
from classes.book_details_page import BookDetailsPage
from classes.borrowed_page import Borrowed_page


class UserPage:
    def __init__(self, window, user, call_back):
        self.window = window
        self.logged_in_user = user
        self.call_back = call_back
        self.user_db = UserDatabase()

    def display_user_page(self):
        self.frame_user_left = tkinter.Frame(self.window)
        self.frame_user_left.pack(side="left", padx=20, pady=20)

        self.frame_user_right = tkinter.Frame(self.window)
        self.frame_user_right.pack(side="right", padx=20, pady=20)

        self.frame_user_top = tkinter.Frame(self.window)
        self.frame_user_top.pack(side="top", padx=20, pady=20)

        self.display_login_signup()
        self.display_book()

    def open_book_detail_page(self, book):
        """Function used to open a page giving details of a book

        Args:
            book : class to homepage inherit
        """

        self.frame_user_right.destroy()
        self.frame_user_left.destroy()
        self.frame_user_top.destroy()
        book_details_page = BookDetailsPage(
            self.window, book, self.display_user_page, self.logged_in_user
        )

        book_details_page.run_display_book()

    def load_books(self):
        """Function that loads books from a JSON file"""
        try:
            with open("./db/book.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                self.books = [
                    Book(
                        item["id"],
                        item["title"],
                        item["author"],
                        item["publication_year"],
                        item["isbn"],
                        item["gender"],
                        item["is_reserved"],
                        item["reserved_by"],
                        item["is_borrowed"],
                        item["borrowed_by"],
                    )
                    for item in data
                ]
        except FileNotFoundError:
            self.books = []

    def display_login_signup(self):
        """Function that displays the library login and registration buttons"""

        # Button Log In
        log_out_button = tkinter.Button(
            self.frame_user_right, text="Log out", command=self.log_out
        )
        log_out_button.pack(pady=10)

    def display_book(self):
        titre = tkinter.Label(
            self.frame_user_top, text="Welcome Member", font=("Arial", 24)
        )
        titre.pack(pady=10)

        # Loading books from a JSON file
        self.load_books()

        # Loop over books and display them
        for book in self.books:
            button_text = f"{book.title} - {book.author}"
            button = tkinter.Button(
                self.frame_user_left,
                text=button_text,
                command=lambda book=book: self.open_book_detail_page(book),
            )
            button.pack(pady=5)

        # Label which will receive information after the user logs in
        self.user_label = tkinter.Label(self.window, text="", font=("Arial", 16))
        self.user_label.pack(pady=10)

    def log_out(self):
        self.frame_user_right.destroy()
        self.frame_user_left.destroy()
        self.frame_user_top.destroy()
        self.logged_in_user = None
        self.call_back()


class AdminPage(UserPage):
    """Class who displays the admin page. This class inherits from the UserPage class"""

    def display_user_page(self):
        super().display_user_page()

        # Button to modify the "users" database
        users_button = tkinter.Button(
            self.frame_user_right, text="Modify user", command=self.manage_db_users
        )
        users_button.pack(pady=10)

        # Button to modify the "book" database
        book_button = tkinter.Button(
            self.frame_user_right, text="Modify book", command=self.manage_db_livres
        )
        book_button.pack(pady=10)

        # book reservation button
        reserve_button = tkinter.Button(
            self.frame_user_right,
            text="Reserve management",
            command=self.open_borrowed_page,
        )
        reserve_button.pack(pady=10)

    def open_borrowed_page(self):
        """Function used to open a page giving details of a book"""
        self.frame_user_right.destroy()
        self.frame_user_left.destroy()
        self.frame_user_top.destroy()
        borrowed_page = Borrowed_page(self.window, self.display_user_page)
        borrowed_page.run_display_borrowed()

    def manage_db_users(self):
        """Function used to manage details of a user in the database"""
        # Charger la base de données des utilisateurs depuis le fichier JSON
        with open("user.json", "r+") as f:
            users_data = json.load(f)

        # Do something with the user database, for example display the data
        for user in users_data:
            print(user)

    def manage_db_livres(self):
        """Function used to manage details of a book in the database"""
        # Load the books database from the JSON file
        with open("book.json", "r+") as f:
            books_data = json.load(f)

        # Do something with the books database, for example display the data
        for book in books_data:
            print(book)
