import tkinter as tk
import json
from tkinter import messagebox
from classes.wishlist import Wishlist


class BookDetailsPage:
    """Class used to display the details of a book on a new page in the library's graphical interface"""

    def __init__(self, window, book, callback, logged_in_user):
        self.window = window
        self.book = book
        self.callback = callback
        self.logged_in_user = logged_in_user
        self.wishlist = Wishlist()

    def run_display_book(self):
        """Function that displays the details of a book"""

        self.frame_detail_left = tk.Frame(self.window)
        self.frame_detail_left.pack(side="left", padx=20, pady=20)

        self.frame_detail_right = tk.Frame(self.window)
        self.frame_detail_right.pack(side="right", padx=20, pady=20)

        self.frame_detail_top = tk.Frame(self.window)
        self.frame_detail_top.pack(side="top", padx=20, pady=20)

        print(self.book.is_reserved)
        print(self.book.reserved_by)

        self.display_book_details()

    def load_database(self):
        with open("./db/book.json", "r") as file:
            data = json.load(file)
        return data

    def save_database(self, data):
        """Function for saving a list of books into a file"""

        with open("./db/book.json", "w") as file:
            json.dump(data, file, indent=4)

    def reserve(self):
        """Function that checks if a book has already been reserved and if the user is logged in"""

        if self.logged_in_user:
            if not self.book.is_reserved:
                self.book.is_reserved = True
                self.book.reserved_by = self.logged_in_user["id"]
                self.update_reserve_cancel_buttons()
                self.window.after(
                    2 * 60 * 60 * 1000, self.cancel_reserve
                )  # Lancer le timer de 2 heures
                messagebox.showinfo("info", "book reserve successfully")
                self.update_database()
                print(self.book.is_reserved)
                print(self.book.reserved_by)
            else:
                messagebox.showinfo("Info", "This book is already booked.")
        else:
            messagebox.showinfo("Info", "You must be logged in to reserve a book.")

    def cancel_reserve(self):
        # Cancel book reservation

        self.book.is_reserved = False
        self.book.reserve_by = None
        self.update_reserve_cancel_buttons()
        messagebox.showinfo("Info", "Booking cancelled with success.")
        self.update_database()
        print(self.book.is_reserved)
        print(self.book.reserved_by)

    def update_reserve_cancel_buttons(self):
        # Check whether the book is reserved and update the button status accordingly

        if self.logged_in_user["id"] == self.book.reserved_by:
            if self.book.is_reserved:
                self.reserve_button.config(
                    state=tk.DISABLED
                )  # Disable the reservation button
                self.cancel_reservation_button.config(
                    state=tk.NORMAL
                )  # Activate the cancel reservation button
            else:
                self.reserve_button.config(
                    state=tk.NORMAL
                )  # Activate the reservation button
                self.cancel_reservation_button.config(
                    state=tk.DISABLED
                )  # Disable the cancel reservation button

    def update_database(self):
        """Function for updating the book database when a reservation has been made"""
        data = self.load_database()
        for book_data in data:
            if book_data["id"] == self.book.book_id:
                book_data["is_reserved"] = self.book.is_reserved
                book_data["reserved_by"] = self.book.reserved_by
                break
        self.save_database(data)

        # Create the widgets and layout for the book details page here

    def display_book_details(self):
        """Function for displaying details of a book"""

        # Title of the book
        title_label = tk.Label(self.frame_detail_top, text=self.book.title)
        title_label.pack()

        # Author of the book
        author_label = tk.Label(
            self.frame_detail_left, text="Author: " + self.book.author
        )
        author_label.pack()

        # Year of publication of the book
        publication_year_label = tk.Label(
            self.frame_detail_left,
            text="Publication year: " + str(self.book.publication_year),
        )
        publication_year_label.pack()

        # ISBN of the book
        isbn_label = tk.Label(self.frame_detail_left, text="ISBN: " + self.book.isbn)
        isbn_label.pack()

        # Category of the book
        category_label = tk.Label(
            self.frame_detail_left, text="Gender: " + self.book.category
        )
        category_label.pack()

        # Return button
        back_button = tk.Button(
            self.frame_detail_left, text="Retour", command=self.return_to_homepage
        )
        back_button.pack()

        # Reservation button
        self.reserve_button = tk.Button(
            self.frame_detail_right, text="reserve", command=self.reserve
        )
        self.reserve_button.pack()

        # Add to wishlist button
        wishlist_button = tk.Button(
            self.frame_detail_right,
            text="Favorite",
            command=lambda: self.wishlist.add_book_to_wishlist(
                self.book, self.logged_in_user
            ),
        )
        wishlist_button.pack()

        # Cancel reservation button
        self.cancel_reservation_button = tk.Button(
            self.frame_detail_right,
            text="Cancel reservation",
            command=self.cancel_reserve,
            state=tk.DISABLED,
        )
        self.cancel_reservation_button.pack()

        # Update the status of the booking and cancellation buttons
        self.update_reserve_cancel_buttons()

    def return_to_homepage(self):
        self.frame_detail_left.destroy()  # Close the book details page
        self.frame_detail_right.destroy()
        self.frame_detail_top.destroy()
        self.callback()  # Call the return function provided by the parent class
