import tkinter
import json
from tkinter import messagebox
from classes.user_db import UserDatabase
from classes.book_details_page import BookDetailsPage


class Borrowed_page:
    def __init__(self, window, callback):
        self.window = window
        self.callback = callback
        self.user_db = UserDatabase()

    def run_display_borrowed(self):
        self.frame_borrowed_left = tkinter.Frame(self.window)
        self.frame_borrowed_left.pack(side="left", padx=20, pady=20)

        self.frame_borrowed_right = tkinter.Frame(self.window)
        self.frame_borrowed_right.pack(side="right", padx=20, pady=20)

        self.frame_borrowed_top = tkinter.Frame(self.window)
        self.frame_borrowed_top.pack(side="top", padx=20, pady=20)

        self.display_borrowed()

    def display_borrowed(self):
        # Load the books from the database
        with open("./db/book.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        # Filter the books to display only the reserved ones
        reserved_books = [book for book in data if book["is_reserved"]]

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
                user = self.user_db.get_user_by_id(book["reserved_by"])

                if user:
                    reserved_by_info = f"reserved by: {user['name']} {user['surname']}"
                else:
                    reserved_by_info = "reserved by: Unknown User"

                book_info = f"Title: {book['title']}\nAuthor: {book['author']}\n{reserved_by_info}"

                book_bouton = tkinter.Button(
                    self.frame_borrowed_left,
                    text=book_info,
                    font=("arial", 12),
                    justify="left",
                    command=lambda book_id=book["id"]: self.show_confirmation_dialog(
                        book_id
                    ),
                )
                book_bouton.pack(pady=5)

    def show_confirmation_dialog(self, book_id):
        # Afficher une boîte de dialogue avec les boutons "Yes" et "No"
        result = messagebox.askyesno(
            "Confirmation", "will you accept the borrow of this book "
        )

        # Vérifier la réponse de l'utilisateur
        if result == True:  # Si l'utilisateur a cliqué sur "Yes"
            self.accept_borrow(book_id)
        else:  # Si l'utilisateur a cliqué sur "No"
            self.deny_borrow(book_id)

    def accept_borrow(self, book_id):
        # Charger les données des livres depuis la base de données
        with open("./db/book.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        # Rechercher le livre par son ID
        book = next((book for book in data if book["id"] == book_id), None)

        # Vérifier si le livre a été trouvé
        if book:
            # Mettre à jour les informations du livre
            book["is_borrowed"] = True
            book["borrowed_by"] = book["reserved_by"]
            book["is_reserved"] = False

            # Enregistrer les modifications dans la base de données
            with open("./db/book.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            # Afficher un message de succès
            messagebox.showinfo("Success", "Book borrow accepted.")
        else:
            # Afficher un message d'erreur si le livre n'a pas été trouvé
            messagebox.showerror("Error", "Book not found.")

    def deny_borrow(self, book_id):
        # Charger les données des livres depuis la base de données
        with open("./db/book.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        # Rechercher le livre par son ID
        book = next((book for book in data if book["id"] == book_id), None)

        # Vérifier si le livre a été trouvé
        if book:
            # Réinitialiser les informations de réservation du livre
            book["is_reserved"] = False
            book["reserved_by"] = None

            # Enregistrer les modifications dans la base de données
            with open("./db/book.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            # Afficher un message de succès
            messagebox.showinfo("Success", "Book borrow denied.")
        else:
            # Afficher un message d'erreur si le livre n'a pas été trouvé
            messagebox.showerror("Error", "Book not found.")

    def back_page(self):
        self.frame_borrowed_left.destroy()
        self.frame_borrowed_right.destroy()
        self.frame_borrowed_top.destroy()
        self.callback()
