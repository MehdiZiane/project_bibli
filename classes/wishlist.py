import json
from tkinter import messagebox


class Wishlist:
    """Class use for create a wishlist for the user"""

    def __init__(self):
        self.books = []

    def add_book_to_wishlist(self, book, logged_in_user):
        """Function enabling the user to add a book he would like to reserve or that he liked in a wishlist

        Args:
            book : the book that the user would like to add to his wishlist
            logged_in_user : to check if the user is logged in
        """
        if logged_in_user == None:
            messagebox.showinfo("info", "Please login to add a book to your favorites")
        else:
            print(book)
            logged_in_user["wishlist"].append(book.title)
            messagebox.showinfo("info", "A book has been added to the wishlist")
            self.save_wishlist(logged_in_user)

    def remove_book(self, books):
        """Function enabling thr user to remove a book from his wishlist

        Args:
            books : the book that the user would like to remove from his wishlist
        """

        if books in self.books:
            self.books.remove(books)
            print("A book has been removed from the wishlist")
        else:
            print("This book is not in the wishlist!")

    def show_wishlist(self):
        """Function enabling the user to view and consult his full wishlist"""

        if self.books:
            print("favorite:")
            for books in self.books:
                print("Title :", books.title)
                print("Author :", books.auteur)
                print("publication year", books.publication_year)
                print("ibsn number", books.isbn)
                print("Gender", books.category)
        else:
            print("The wish list is empty.")

    def save_wishlist(self, logged_in_user):
        """Function for saving the books the user would like in a wishlist

        Args:
            logged_in_user : to search for logged-in user information
        """
        with open("./db/user.json", "r") as file:
            users = json.load(file)

        for user_data in users:
            if user_data["id"] == logged_in_user["id"]:
                user_data["wishlist"] = logged_in_user["wishlist"]
                break

        with open("./db/user.json", "w") as file:
            json.dump(users, file, indent=4)
