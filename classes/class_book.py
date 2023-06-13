## initialisation de la class Book
class Book:
    #initialisation de la méthode "book" en fonction de la DataBase
    def __init__(self, book_id, title, author, publication_year, isbn, category, is_reserved=False, reserved_by=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.category = category
        self.is_reserved = is_reserved
        self.reserved_by = reserved_by
    
    def reserve_book(self):
        self.is_reserved = True
    
    def cancel_reservation(self):
        self.is_reserved = False
        
    def add_to_wishlist(self):
        self.add_wishlist = True
        
