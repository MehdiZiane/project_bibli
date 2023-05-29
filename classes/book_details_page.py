import tkinter as tk
import json
from classes.class_book import Book

class BookDetailsPage():
    def __init__(self):
        self.book = []

    def load_books(self):
        try:
            with open("./db/book.json", "r") as file:
                data = json.load(file)
                self.book = [Book(item['id'], item['titre'], item['auteur'], item['annee_publication'], item['isbn'], item['categorie']) for item in data]
                print(self.books)
        except FileNotFoundError:
            self.books = []
        
        # Créez les widgets et la mise en page pour la page des détails du livre ici

        self.load_books

        # Titre du livre
        title_label = tk.Label(self, text="Titre: " + self.book.titre)
        title_label.pack()

        # Auteur du livre
        author_label = tk.Label(self, text="Auteur: " + self.book.author)
        author_label.pack()

        # Année de publication du livre
        publication_year_label = tk.Label(self, text="Année de publication: " + str(self.book.publication_year))
        publication_year_label.pack()

        # ISBN du livre
        isbn_label = tk.Label(self, text="ISBN: " + self.book.isbn)
        isbn_label.pack()

        # Catégorie du livre
        category_label = tk.Label(self, text="Catégorie: " + self.book.category)
        category_label.pack()

        # Bouton de retour
        back_button = tk.Button(self, text="Retour", command=self.return_to_homepage)
        back_button.pack()

    def return_to_homepage(self):
        self.destroy()  # Fermer la page des détails du livre
        self.return_callback()  # Appeler la fonction de retour fournie par la classe parent