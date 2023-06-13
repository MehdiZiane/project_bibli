## Book classs initialization
class Book:
    """ Class that describes books in the library with properties
    """
    
    # initialization of the "book" method according to the DataBase
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
        """ Function use to reserve a book 
        """
        self.is_reserved = True
    
    def cancel_reservation(self):
        """ Function use to cancel a reservation of a book
        """
        self.is_reserved = False
        
    def add_to_wishlist(self):
        """ Function use to add a book to a wishlist
        """
        self.add_wishlist = True
        
