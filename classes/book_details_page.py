import tkinter as tk
import json
from classes.class_book import Book
from classes.wishlist import Wishlist

class BookDetailsPage():
    
    def __init__(self, window, book, callback):
        
        self.window = window
        self.book = book
        self.callback = callback
        self.logged_in_user = None
        self.wishlist = Wishlist()

    def run_display_book(self):
        
        self.frame_detail_left = tk.Frame(self.window)
        self.frame_detail_left.pack(side='left', padx=20, pady=20)

        self.frame_detail_right = tk.Frame(self.window)
        self.frame_detail_right.pack(side='right', padx=20, pady=20)

        self.display_book_details()

    def load_books(self):
        try:
            with open("./db/book.json", "r") as file:
                data = json.load(file)
                self.book = [Book(item['id'], item['titre'], item['auteur'], item['annee_publication'], item['isbn'], item['categorie']) for item in data]
        except FileNotFoundError:
            self.book = []
        
        # Créez les widgets et la mise en page pour la page des détails du livre ici
    def display_book_details(self):
        
        self.load_books()
        
        # Titre du livre
        title_label = tk.Label(self.frame_detail_left, text="Titre: " + self.book[0].title)
        title_label.pack()

        # Auteur du livre
        author_label = tk.Label(self.frame_detail_left, text="Auteur: " + self.book[0].author)
        author_label.pack()

        # Année de publication du livre
        publication_year_label = tk.Label(self.frame_detail_left, text="Année de publication: " + str(self.book[0].publication_year))
        publication_year_label.pack()

        # ISBN du livre
        isbn_label = tk.Label(self.frame_detail_left, text="ISBN: " + self.book[0].isbn)
        isbn_label.pack()

        # Catégorie du livre
        category_label = tk.Label(self.frame_detail_left, text="Catégorie: " + self.book[0].category)
        category_label.pack()

        # Bouton de retour
        back_button = tk.Button(self.frame_detail_left, text="Retour", command=self.return_to_homepage)
        back_button.pack()
        
        #Bouton pour réserver
        reserve_button = tk.Button(self.frame_detail_right, text="reserve")
        reserve_button.pack()
        
        #Bouton pour annuler une réservation
        cancel_reservation_button = tk.Button(self.frame_detail_right, text="Cancel reservation")
        cancel_reservation_button.pack()
        
        #Bouton d'ajout à la liste de souhaits
        wishlist_button = tk.Button(self.frame_detail_right, text="Favoris", command=lambda: self.wishlist.ajouter_livre(self.book))
        wishlist_button.pack()
        
    def return_to_homepage(self):
        self.frame_detail_left.destroy()  # Fermer la page des détails du livre
        self.frame_detail_right.destroy()
        self.callback()  # Appeler la fonction de retour fournie par la classe parent
        
            