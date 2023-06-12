import tkinter
import json
from tkinter import messagebox
from classes.homepage import Homepage
from classes.class_book import Book
from classes.user_db import UserDatabase
from classes.window import Window
from classes.class_user import User
from classes.book_details_page import BookDetailsPage

class user_page():
    def __init__(self,window,user):
        self.window = window
        self.logged_in_user = user
        self.user_db = UserDatabase()
        
    def display_user_page(self):
        self.frame_user_left = tkinter.Frame(self.window)
        self.frame_user_left.pack(side='left', padx=20, pady=20)
        
        self.frame_user_right = tkinter.Frame(self.window)
        self.frame_user_right.pack(side='right', padx=20, pady=20)
        
        self.frame_user_top = tkinter.Frame(self.window)
        self.frame_user_top.pack(side='top', padx=20, pady=20)
        
    def open_book_detail_page(self, book):
        """ Function used to open a page giving details of a book 

        Args:
            book : class to homepage inherit
        """
        
        self.frame_user_right.destroy()
        self.frame_user_left.destroy()
        self.frame_user_top.destroy()
        book_details_page = BookDetailsPage(self.window, book, self.run_display, self.logged_in_user)
        book_details_page.run_display_book()
    
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
        
    def load_books(self):
        try:
            with open("./db/book.json", "r") as file:
                data = json.load(file)
                self.books = [Book(item['id'], item['titre'], item['auteur'], item['annee_publication'], item['isbn'], item['categorie']) for item in data]
                print(self.books)
        except FileNotFoundError:
            self.books = []
            
    def display_login_signup(self):
        """ Function that displays the library login and registration buttons
        """
        
        self.frame_user_right = tkinter.Frame(self.window)
        self.frame_user_right.pack(side = 'right', padx=20, pady=20)
        
        # Button Log In
        log_in_button = tkinter.Button(self.frame_user_right, text='Log In', command=self.login)
        log_in_button.pack(pady=10)

        # Button Sign Up
        sign_up_button = tkinter.Button(self.frame_user_right, text='Sign Up', command=self.create_account_dialog)
        sign_up_button.pack(pady=10)
        
    def display_book(self):

        self.frame_user_top = tkinter.Frame(self.window)
        self.frame_user_top.pack(side='top', padx=20, pady=20)
        titre = tkinter.Label(self.frame_user_top, text="Bienvenue dans la bibliothèque", font=("Arial", 24))
        titre.pack(pady=20)

        # Creating the left frame for displaying books
        self.frame_user_left = tkinter.Frame(self.window)
        self.frame_user_left.pack(side='left', padx=20, pady=20)
        
        # Loading books from a JSON file
        self.load_books()

        # Loop over books and display them
        for book in self.books:
            button_text= f"{book.title} - {book.author}"
            button = tkinter.Button(self.frame_user_left, text=button_text, command=lambda book=book: self.open_book_detail_page(book))
            button.pack(pady=5)
        
        # Label which will receive information after the user logs in
        self.user_label = tkinter.Label(self.window, text='', font=("Arial", 16))
        self.user_label.pack(pady=10)
        
    def run_display(self):
        self.display_book()
        self.display_login_signup()
        
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
        
        
    


class Admin_Page(user_page):
    def __init__(self):
        super().__init__()
        self.window.title("Admin_Page")
        self.window.configure(bg="#15c3f2")
        
        
   
    
        
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


        # Bouton pour modifier la base de données "users"
        users_button = tkinter.Button(self.frame_user_right, text="Modifier Users", command=self.gestion_db_users)
        users_button.pack(pady=10)

        # Bouton pour modifier la base de données "book"
        book_button = tkinter.Button(self.frame_user_right, text="Modifier Book", command=self.gestion_db_livres)
        book_button.pack(pady=10)
        
        #bouton pour reserver un livre
        reserve_button = tkinter.Button(self.frame_user_right, text="Reserver un livre", command=self.reserver_livre)
        reserve_button.pack(pady=10)
        

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