import json
from classes.class_book import Book

class BookDatabase:
    """ Class use to manage the book database
    """
    def __init__(self):
        self.books = self.load_books_from_file()
    
    def load_books_from_file(self):
        """ Function enabling the user to search a book in the library 

        Returns:
            _type_: if a book is not registered in the database, the programme returns to the previous display.
        """
        try:
            with open("./db/book.json", "r") as file:
                self.books = json.load(file)
                return self.books
        except FileNotFoundError:
            return []

    def save_books_to_file(self):
        """ Function for saving books in a stocking
        """
        with open("./db/book.json", "w") as file:
            json.dump(self.books, file, indent=4)
    
    def ajouter_livre(self, book_id, title, author, publication_year, isbn, category):
        """ Function for adding a book to the database

        Args:
            book_id (?): to enter the id of a book
            title (char): to enter a title of a book
            author (char): to enter the author of a book
            publication_year (int): to enter the year of publication of a book
            isbn (bool): to enter the international standard book number of a book
            category (char): to enter the category of a book
        """
        livre = {
            'id': book_id,
            'titre': title,
            'auteur': author,
            'annee_publication': publication_year,
            'isbn': isbn,
            'categorie': category
        }
        # Self.load_books_from_file()
        self.books.append(livre)
        self.save_books_to_file()
    
    def supprimer_livre(self, book_id):
        # Search for the book to be deleted
        index = None
        for i, livre in enumerate(self.books):
            if livre['id'] == book_id:
                index = i
                break

        if index is not None:
            # Remove the book from the list
            del self.books[index]
            # Save changes in the JSON file
            self.save_books_to_file()
            print(f"Livre avec ID {book_id} supprimé.")
        else:
            print(f"Livre avec ID {book_id} introuvable.")

class Wishlist(Book):
    """ Class use for create a wishlist

    Args:
        Book (char): class to wishlist inherit
    """
    def __init__(self):
        self.books = []

    def ajouter_livre(self, books):
        """ Function enabling the user to add a book he would like to reserve or that he liked in a wishlist 
        """
        
        self.books.append(books)
        print("Un livre a été ajouté dans la liste de souhaits.")

    def retirer_livre(self, books):
        """ Function enabling thr user to remove a book from his wishlist 
        """
        
        if books in self.books:
            self.books.remove(books)
            print("Un livre a été retiré de la liste de souhaits.")
        else:
            print("Ce livre n'est pas dans la liste de souhaits !")

    def afficher_liste(self):
        """ Function enabling the user to view and consult his full wishlist
        """
        
        if self.books:
            print("Liste de souhaits :")
            for books in self.books:
                print("Titre :", books.title)
                print("Auteur :", books.auteur)
                print("Année de publication", books.publication_year)
                print("Numéro ibsn", books.isbn)
                print("Genre", books.category)
        else:
            print("La liste de souhaits est vide.")