import tkinter
import json
from classes.homepage import Homepage
from classes.class_book import Book
from classes.user_db import UserDatabase
from classes.window import Window
from classes.class_user import User
from classes.book_details_page import BookDetailsPage

class Admin_Page(Homepage):
    def __init__(self):
        super(Homepage).__init__()
        self.window.title("Admin_Page")
        self.window.configure(bg="#15c3f2")
        self.run_display()
        
        #création fenêtre "Admin Page
        Admin_Window = tkinter()
        
        # # Affichage de la page
        # Admin_Window.title('Bibliothèque des 4 rives - Admin Page')
        # Admin_Window.geometry('1280x720')
        # Admin_Window.minsize(720, 480)
        # Admin_Window.config(background='#15c3f2')
        # label_title = Admin_Window.Label(Admin_Window, text='Bienvenue sur la page Admin', font=('Arial', 24), bg='#15c3f2', fg='red')
        # label_title.pack(expand='yes')
        # # création du bouton "Gestion DB livres"
        # Frame_button_1 = Admin_Window.Frame(Admin_Window, bg='#15c3f2')
        # Frame_button_1.pack(expand='yes', side = 'left', padx=10, pady=10)
        # DB_Book_Button = Admin_Window.Button(Frame_button_1, text='Gestion DB livres', font=('Arial', 10), command=self.gestion_db_livres)
        # DB_Book_Button.pack(expand='yes', padx=40)
        # # création du bouton "Gestion DB users"
        # Frame_button_2 = Admin_Window.Frame(Admin_Window, bg='#15c3f2')
        # Frame_button_2.pack(expand='yes', side = 'right', padx=10, pady=10)
        # DB_User_Button = Admin_Window.Button(Frame_button_2, text='Gestion DB users', font=('Arial', 10), command=self.gestion_db_users)
        # DB_User_Button.pack(expand='yes', padx=40)
        # Admin_Window.mainloop()
        
        # Création du cadre principal
        self.frame = tkinter.Frame(self.window, bg="#15c3f2")
        self.frame.pack(padx=20, pady=20)

        # Bouton pour modifier la base de données "users"
        users_button = tkinter.Button(self.frame, text="Modifier Users", command=self.gestion_db_users)
        users_button.pack(pady=10)

        # Bouton pour modifier la base de données "book"
        book_button = tkinter.Button(self.frame, text="Modifier Book", command=self.gestion_db_livres)
        book_button.pack(pady=10)

    def run_display(self):
        self.window.mainloop()

    def gestion_db_users(self):
        # Charger la base de données des utilisateurs depuis le fichier JSON
        with open('user.json', 'r+') as f:
            users_data = json.load(f)

        # Faites quelque chose avec la base de données des utilisateurs, par exemple afficher les données
        for user in users_data:
            print(user)

    def gestion_db_livres(self):
        # Charger la base de données des livres depuis le fichier JSON
        with open('book.json', 'r+') as f:
            books_data = json.load(f)

        # Faites quelque chose avec la base de données des livres, par exemple afficher les données
        for book in books_data:
            print(book)