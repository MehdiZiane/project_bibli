## Book classs initialization
class Book:
    """Class that describes books in the library with properties"""

    # initialization of the "book" method according to the DataBase
    def __init__(
        self,
        book_id,
        title,
        author,
        publication_year,
        isbn,
        category,
        is_reserved=False,
        reserved_by=None,
        is_borrowed=False,
        borrowed_by=None,
    ):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.category = category
        self.is_reserved = is_reserved
        self.reserved_by = reserved_by
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by

    def reserve_book(self):
        """Function use to reserve a book"""
        self.is_reserved = True

    def cancel_reservation(self):
        """Function use to cancel a reservation of a book"""
        self.is_reserved = False

    def add_to_wishlist(self):
        """Function use to add a book to a wishlist"""
        self.add_wishlist = True

    def borrow_book(self, user):
        """Function used to borrow a book"""
        if not self.is_reserved and not self.is_borrowed:
            self.is_borrowed = True
            self.borrowed_by = user
            # Update information about the user who borrowed the book

    def return_book(self):
        """Function used to return a borrowed book"""
        if self.is_borrowed:
            self.is_borrowed = False
            self.borrowed_by = None
            # Update information about the user who borrowed the book
