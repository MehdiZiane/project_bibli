import tkinter
import json


class Borrowed_page:
    def __init__(self, window, callback):
        self.window = window
        self.callback = callback

    def run_display_borrowed(self):
        self.frame_borrowed_left = tkinter.Frame(self.window)
        self.frame_borrowed_left.pack(side="left", padx=20, pady=20)

        self.frame_borrowed_right = tkinter.Frame(self.window)
        self.frame_borrowed_right.pack(side="right", padx=20, pady=20)

        self.frame_borrowed_top = tkinter.Frame(self.window)
        self.frame_borrowed_top.pack(side="top", padx=20, pady=20)

        self.display_borrowed()

    def display_borrowed(self):
        # Load the books from the database
        with open("./db/book.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        # Filter the books to display only the borrowed ones
        borrowed_books = [book for book in data if book["is_borrowed"]]

        return_button = tkinter.Button(
            self.frame_borrowed_right,
            text="Return",
            command=self.back_page,
        )
        return_button.pack(pady=5)

        if not borrowed_books:
            # Display a message if there are no borrowed books
            no_books_label = tkinter.Label(
                self.frame_borrowed_top,
                text="No books are currently borrowed.",
                font=("Arial", 16),
            )
            no_books_label.pack(pady=10)
        else:
            # Display the borrowed books
            for book in borrowed_books:
                book_info = f"Title: {book['title']}\nAuthor: {book['author']}\nBorrowed by: {book['borrowed_by']}"
                book_label = tkinter.Label(
                    self.frame_borrowed_left,
                    text=book_info,
                    font=("Arial", 12),
                    justify="left",
                )
                book_label.pack(pady=5)

    def back_page(self):
        self.frame_borrowed_left.destroy()
        self.frame_borrowed_right.destroy()
        self.frame_borrowed_top.destroy()
        self.callback()
