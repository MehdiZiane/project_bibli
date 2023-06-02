import tkinter as tk
import json
from classes.class_book import Book

class BookDetailsPage():
    
    def __init__(self, window, book, callback, logged_in_user=None):
        
        self.window = window
        self.book = book
        self.callback = callback
        self.logged_in_user = logged_in_user

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
    
    def reserve(self):
        if not self.book[0].is_reserved:
        # Vérifier si un utilisateur est connecté
            if self.logged_in_user:
                # Réserver le livre et attribuer l'identifiant de l'utilisateur
                self.book[0].is_reserved = True
                self.book[0].reserve_by = self.logged_in_user['id']
                self.update_reserved_label()

                # Lancer le timer de 2 heures
                self.window.after(2 * 60 * 60 * 1000, self.cancel_reservation)
            else:
                tk.messagebox.showinfo('Info', 'Vous devez être connecté pour réserver un livre.')
        else:
            tk.messagebox.showinfo('Info', 'Ce livre est déjà réservé.')

    def cancel_reserve(self):
        # Annuler la réservation du livre
        self.book[0].cancel_reservation()
        tk.messagebox.showinfo('Information', 'Réservation annulée avec succès.')
        self.update_reserve_cancel_buttons()  # Mettre à jour les boutons de réservation et d'annulation de réservation
    
    def update_reserve_cancel_buttons(self):
        # Vérifier si le livre est réservé et mettre à jour les états des boutons en conséquence
        if self.book[0].is_reserved:
            self.reserve_button.config(state=tk.DISABLED)  # Désactiver le bouton de réservation
            self.cancel_button.config(state=tk.NORMAL)  # Activer le bouton d'annulation de réservation
        else:
            self.reserve_button.config(state=tk.NORMAL)  # Activer le bouton de réservation
            self.cancel_button.config(state=tk.DISABLED)  # Désactiver le bouton d'annulation de réservation
        
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

        reserve_button = tk.Button(self.frame_detail_right, text="reserve", command=self.reserve)
        reserve_button.pack()

        cancel_reserve_button = tk.Button(self.frame_detail_right, text='cancel reserve', command= self.cancel_reserve)
        cancel_reserve_button.pack()

    def return_to_homepage(self):
        self.frame_detail_left.destroy()  # Fermer la page des détails du livre
        self.frame_detail_right.destroy()
        self.callback()  # Appeler la fonction de retour fournie par la classe parent