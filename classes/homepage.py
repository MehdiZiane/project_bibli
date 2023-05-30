import tkinter
import json
from tkinter import messagebox
from classes.class_book import Book
from classes.user_db import UserDatabase
from classes.class_user import User
from classes.window import Window
from classes.book_details_page import BookDetailsPage

class Homepage(Window):
    def __init__(self):
        super().__init__()
        self.books = []
        self.user_db = UserDatabase()
        self.display_book()
        self.display_login_signup()
    
    def display_book(self):

        self.frame_titre = tkinter.Frame(self.window)
        self.frame_titre.pack(side='top', padx=20, pady=20)
        titre = tkinter.Label(self.frame_titre, text="Bienvenue dans la bibliothèque", font=("Arial", 24))
        titre.pack(pady=20)

        # Création du cadre gauche pour afficher les livres
        self.frame_left = tkinter.Frame(self.window)
        self.frame_left.pack(side='left', padx=20, pady=20)
        
        # Charger les livres à partir du fichier JSON
        self.load_books()

        # Boucle sur les livres et les afficher
        for book in self.books:
            button_text= f"{book.title} - {book.author}"
            button = tkinter.Button(self.frame_left, text=button_text, command=lambda book=book: self.open_book_detail_page(book))
            button.pack(pady=5)
        
        #label qui accueillera les info suite a la connexion de l user
        self.user_label = tkinter.Label(self.window, text='', font=("Arial", 16))
        self.user_label.pack(pady=10)

    def open_book_detail_page(self, book):
        
        self.frame_right.destroy()
        self.frame_left.destroy()
        self.frame_titre.destroy()
        book_details_page = BookDetailsPage(self.window, book)
        book_details_page.display_book_details()
    
    def display_login_signup(self):
        
        self.frame_right = tkinter.Frame(self.window)
        self.frame_right.pack(side = 'right', padx=20, pady=20)
        
        # Bouton Log In
        log_in_button = tkinter.Button(self.frame_right, text='Log In', command=self.login)
        log_in_button.pack(pady=10)

        # Bouton Sign Up
        sign_up_button = tkinter.Button(self.frame_right, text='Sign Up', command=self.create_account_dialog)
        sign_up_button.pack(pady=10)

    
    def load_books(self):
        try:
            with open("./db/book.json", "r") as file:
                data = json.load(file)
                self.books = [Book(item['id'], item['titre'], item['auteur'], item['annee_publication'], item['isbn'], item['categorie']) for item in data]
                print(self.books)
        except FileNotFoundError:
            self.books = []

    def create_account(self, nom, prenom, email, password, dialog):
        self.user_db.create_account(nom, prenom, email, password)
        messagebox.showinfo('Success', 'Account created successfully!')
        dialog.destroy()
    
    def create_account_dialog(self):
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
        # Utilisez la classe UserDatabase pour vérifier l'authentification
        user = self.user_db.authenticate_user(email, password)
        if user:
            messagebox.showinfo('Success', 'Login successful!')
            self.user_label.config(text=f"Welcome, {user['prenom']} {user['nom']}")  # Mettez à jour le label avec les informations de l'utilisateur
        else:
            messagebox.showerror('Error', 'Invalid email or password.')
        
        dialog.destroy()