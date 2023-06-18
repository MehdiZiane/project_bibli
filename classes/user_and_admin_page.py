import tkinter
import json
from tkinter import messagebox
from classes.class_book import Book
from classes.user_db import UserDatabase
from classes.class_user import User
from classes.book_details_page import BookDetailsPage


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
        book_details_page = BookDetailsPage(self.window, book, self.display_user_page)

        # Vérifiez si un utilisateur est connecté et passez-le à la page des détails du livre
        if self.logged_in_user:
            book_details_page.set_logged_in_user(self.logged_in_user)

        book_details_page.run_display_book()

    def load_books(self):
        try:
            with open("./db/book.json", "r") as file:
                data = json.load(file)
                self.books = [
                    Book(
                        item["id"],
                        item["titre"],
                        item["auteur"],
                        item["annee_publication"],
                        item["isbn"],
                        item["categorie"],
                    )
                    for item in data
                ]
                print(self.books)
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
            self.frame_user_top, text="Bienvenue membre", font=("Arial", 24)
        )
        titre.pack(pady=20)

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
        print(self.logged_in_user)


class AdminPage(UserPage):
    def display_user_page(self):
        super().display_user_page()

        # Bouton pour modifier la base de données "users"
        users_button = tkinter.Button(
            self.frame_user_right, text="Modifier Users", command=self.gestion_db_users
        )
        users_button.pack(pady=10)

        # Bouton pour modifier la base de données "book"
        book_button = tkinter.Button(
            self.frame_user_right, text="Modifier Book", command=self.gestion_db_livres
        )
        book_button.pack(pady=10)

        # bouton pour reserver un livre
        reserve_button = tkinter.Button(
            self.frame_user_right, text="Reserver un livre", command=self.reserver_livre
        )
        reserve_button.pack(pady=10)

    def gestion_db_users(self):
        # Charger la base de données des utilisateurs depuis le fichier JSON
        with open("user.json", "r+") as f:
            users_data = json.load(f)

        # Faites quelque chose avec la base de données des utilisateurs, par exemple afficher les données
        for user in users_data:
            print(user)

    def gestion_db_livres(self):
        # Charger la base de données des livres depuis le fichier JSON
        with open("book.json", "r+") as f:
            books_data = json.load(f)

        # Faites quelque chose avec la base de données des livres, par exemple afficher les données
        for book in books_data:
            print(book)
