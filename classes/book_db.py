import json
from classes.class_book import Book

class BookDatabase:
    def __init__(self):
        self.books = self.load_books_from_file()
    
    def load_books_from_file(self):
        try:
            with open("./db/book.json", "r") as file:
                self.books = json.load(file)
                return self.books
        except FileNotFoundError:
            return []

    def save_books_to_file(self):
        with open("./db/book.json", "w") as file:
            json.dump(self.books, file, indent=4)
    
    def ajouter_livre(self, book_id, title, author, publication_year, isbn, category):
        livre = {
            'id': book_id,
            'titre': title,
            'auteur': author,
            'annee_publication': publication_year,
            'isbn': isbn,
            'categorie': category
        }
        #self.load_books_from_file()
        self.books.append(livre)
        self.save_books_to_file()
    
    def supprimer_livre(self, book_id):
        # Recherche du livre à supprimer
        index = None
        for i, livre in enumerate(self.books):
            if livre['id'] == book_id:
                index = i
                break

        if index is not None:
            # Suppression du livre de la liste
            del self.books[index]
            # Enregistrement des modifications dans le fichier JSON
            self.save_books_to_file()
            print(f"Livre avec ID {book_id} supprimé.")
        else:
            print(f"Livre avec ID {book_id} introuvable.")

class Wishlist(Book):
    def __init__(self):
        self.books = []

    def ajouter_livre(self, books):
        """Cette fontion permet à l'utilisateur d"ajouter un livre qu'il aimerait réserver ou qu'il a aimé dans une wishlist"""
        
        self.books.append(books)
        print("Un livre a été ajouté dans la liste de souhaits.")

    def retirer_livre(self, books):
        """Cette fonction permet à l'utilisateur de supprimer un livre de sa wishlist. 
        Si le livre n'est pas dans la DB de la wishlist, l'utilisateur recevra un message le notifiant de l'échec"""
        
        if books in self.books:
            self.books.remove(books)
            print("Un livre a été retiré de la liste de souhaits.")
        else:
            print("Ce livre n'est pas dans la liste de souhaits !")

    def afficher_liste(self):
        """Cette fonction permet à l'utilisateur d'afficher et de consulter sa wishlist complète.
        Si la liste de souhaits ne contient pas de livres, l'utilisateur recevra une notification"""
        
        if self.books:
            print("Liste de souhaits :")
            for books in self.books:
                print("Titre :", books.titre)
                print("Auteur :", books.auteur)
                print()
        else:
            print("La liste de souhaits est vide.")