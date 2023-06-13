import json
from tkinter import messagebox

class Wishlist:
    """ Class use for create a wishlist
    """
    
    def __init__(self):
        self.books = []

    def ajouter_livre(self, book, logged_in_user):
        """ Function enabling the user to add a book he would like to reserve or that he liked in a wishlist 
        """
        if logged_in_user == None:
            messagebox.showinfo('info', 'Veuillez vous connecter pour ajouter un livre à vos favoris')
        else:
            print(book)
            self.books.append(book)
            print("Un livre a été ajouté dans la liste de souhaits.")
            self.sauvegarder_wishlist()
    

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
            
    def sauvegarder_wishlist(self):
        with open("user.json", "w") as file:
            json.dump(self.books, file)