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