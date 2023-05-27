## initialisation de la class Book
class Book:
    #initialisation de la méthode "book" en fonction de la DataBase
    def __init__(self, book_id, title, author, publication_year, isbn, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.category = category
        
