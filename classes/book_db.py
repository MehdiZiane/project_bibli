import json
from classes.class_book import Book


class BookDatabase:
    """Class use to manage the book database"""

    def __init__(self):
        self.books = self.load_books_from_file()

    def load_books(self):
        try:
            with open("./db/book.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                book = [
                    Book(
                        item["id"],
                        item["title"],
                        item["author"],
                        item["publication_year"],
                        item["isbn"],
                        item["gender"],
                        item["is_reserved"],
                        item["reserved_by"],
                        item["is_borrowed"],
                        item["borrowed_by"],
                    )
                    for item in data
                ]
                return book
        except FileNotFoundError:
            self.books = []

    def load_books_from_file(self):
        """Function that open a file to read a book

        Returns: if a book is not registered in the database, the programme returns to the previous display.
        """
        try:
            with open("./db/book.json", "r") as file:
                self.books = json.load(file)
                return self.books
        except FileNotFoundError:
            return []

    def save_books_to_file(self):
        """Function for saving books in a stocking"""
        with open("./db/book.json", "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, book_id, title, author, publication_year, isbn, category):
        """Function for adding a book to the database

        Args:
            book_id : to enter the id of a book
            title (char): to enter a title of a book
            author (char): to enter the author of a book
            publication_year (int): to enter the year of publication of a book
            isbn (bool): to enter the international standard book number of a book
            category (char): to enter the category of a book
        """
        livre = {
            "id": book_id,
            "titre": title,
            "auteur": author,
            "annee_publication": publication_year,
            "isbn": isbn,
            "categorie": category,
        }

        # Self.load_books_from_file()
        self.books.append(livre)
        self.save_books_to_file()

    def delete_book(self, book_id):
        """Function for delete a book from the library

        Args:
            book_id : id of the book to be deleted
        """

        # Search for the book to be deleted
        index = None
        for i, livre in enumerate(self.books):
            if livre["id"] == book_id:
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
