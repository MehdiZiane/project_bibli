import tkinter
import json
from tkinter import messagebox
from classes.class_book import Book
from classes.user_db import UserDatabase
from classes.class_user import User
from classes.window import Window
from classes.book_details_page import BookDetailsPage

class Homepage(Window):
    """ Class use for display the homepage of your library app

    Args:
        Window : class to homepage inherit
    """
    def __init__(self):
        super().__init__()
        self.books = []
        self.user_db = UserDatabase()
        self.book_details_page = None
        self.logged_in_user = None
        self.run_display()
    
    def run_display(self):
        self.display_book()
        self.display_login_signup()
    
    def display_book(self):

        self.frame_titre = tkinter.Frame(self.window)
        self.frame_titre.pack(side='top', padx=20, pady=20)
        titre = tkinter.Label(self.frame_titre, text="Bienvenue dans la bibliothèque", font=("Arial", 24))
        titre.pack(pady=20)

        # Creating the left frame for displaying books
        self.frame_left = tkinter.Frame(self.window)
        self.frame_left.pack(side='left', padx=20, pady=20)
        
        # Loading books from a JSON file
        self.load_books()

        # Loop over books and display them
        for book in self.books:
            button_text= f"{book.title} - {book.author}"
            button = tkinter.Button(self.frame_left, text=button_text, command=lambda book=book: self.open_book_detail_page(book))
            button.pack(pady=5)
        
        # Label which will receive information after the user logs in
        self.user_label = tkinter.Label(self.window, text='', font=("Arial", 16))
        self.user_label.pack(pady=10)

    def open_book_detail_page(self, book):
        """ Function used to open a page giving details of a book 

        Args:
            book : class to homepage inherit
        """
        
        self.frame_right.destroy()
        self.frame_left.destroy()
        self.frame_titre.destroy()
        self.book_details_page = BookDetailsPage(self.window, book, self.run_display)
        
        # Check if a user is logged in and pass the argument to the book detail page
        if self.logged_in_user:
            self.book_details_page.set_logged_in_user(self.logged_in_user)
        
        self.book_details_page.run_display_book()
    
    def display_login_signup(self):
        """ Function that displays the library login and registration buttons
        """
        
        self.frame_right = tkinter.Frame(self.window)
        self.frame_right.pack(side = 'right', padx=20, pady=20)
        
        # Button Log In
        log_in_button = tkinter.Button(self.frame_right, text='Log In', command=self.login)
        log_in_button.pack(pady=10)

        # Button Sign Up
        sign_up_button = tkinter.Button(self.frame_right, text='Sign Up', command=self.create_account_dialog)
        sign_up_button.pack(pady=10)

    
    def load_books(self):
        try:
            with open("./db/book.json", "r",encoding="utf-8") as file:
                data = json.load(file)
                self.books = [Book(item['id'], item['titre'], item['auteur'], item['annee_publication'], item['isbn'], item['categorie'], item['is_reserved'], item['reserved_by']) for item in data]
                print(self.books)
        except FileNotFoundError:
            self.books = []

    def create_account(self, nom, prenom, email, password, dialog):
        """ Function that allows the user to enter the data needed to create an account in the library.

        Args:
            nom (char): the name the user will choose
            prenom (char): the first name that the user will choose
            email (char): the email address that the user will choose
            password (char): the password that the user will choose
            dialog : the message displayed to the user
        """
        self.user_db.create_account(nom, prenom, email, password)
        messagebox.showinfo('Success', 'Account created successfully!')
        dialog.destroy()
    
    def create_account_dialog(self):
        """ Function that displays the dialog box where the user can enter him details to create a user account.
        """
        dialog = tkinter.Toplevel()
        dialog.title('Create Account')

        nom_label = tkinter.Label(dialog, text='Nom:')
        nom_label.pack()
        nom_entry = tkinter.Entry(dialog)
        nom_entry.pack()

        prenom_label = tkinter.Label(dialog, text='Prénom:')
        prenom_label.pack()
        prenom_entry = tkinter.Entry(dialog)
        prenom_entry.pack()

        email_label = tkinter.Label(dialog, text='Email:')
        email_label.pack()
        email_entry = tkinter.Entry(dialog)
        email_entry.pack()

        password_label = tkinter.Label(dialog, text='Password:')
        password_label.pack()
        password_entry = tkinter.Entry(dialog, show='*')
        password_entry.pack()

        create_button = tkinter.Button(dialog, text='Create Account', command=lambda: self.create_account(nom_entry.get(), prenom_entry.get(), email_entry.get(), password_entry.get(), dialog))
        create_button.pack(pady=10)
    
    def login(self):
        """ Function enablling the user to connect to his user account in the library
        """
        dialog = tkinter.Toplevel()
        dialog.title('Log In')

        email_label = tkinter.Label(dialog, text='Email:')
        email_label.pack()
        email_entry = tkinter.Entry(dialog)
        email_entry.pack()

        password_label = tkinter.Label(dialog, text='Password:')
        password_label.pack()
        password_entry = tkinter.Entry(dialog, show='*')
        password_entry.pack()

        login_button = tkinter.Button(dialog, text='Log In', command=lambda: self.check_login(email_entry.get(), password_entry.get(), dialog))
        login_button.pack(pady=10)

    def check_login(self, email, password, dialog):
        """ Function that checks the information the user has entered for their connection

        Args:
            email (char): the email address used by thr user
            password (char): the password used by the user
            dialog : the message displayed to the user
        """
        
        # Use the UserDatabase class to check authentication
        user = self.user_db.authenticate_user(email, password)
        if user:
            messagebox.showinfo('Success', 'Login successful!')
            self.logged_in_user = user
            self.user_label.config(text=f"Welcome, {user['prenom']} {user['nom']}")  # Mettez à jour le label avec les informations de l'utilisateur
            if user['admin'] == True:
                print ("user['prenom'] is an admin")                #print(f"{user['prenom']} is an admin")
                #Admin_Page()
            else:
                print(f"{user['prenom']} is not an admin")
        else:
            messagebox.showerror('Error', 'Invalid email or password.')
        
        dialog.destroy()
        
    