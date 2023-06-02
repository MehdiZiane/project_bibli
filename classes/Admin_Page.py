from tkinter import *
import json
# from classes.class_book import Book
# from classes.user_db import UserDatabase
# from classes.window import Window
# from classes.class_user import User
# from classes.book_details_page import BookDetailsPage

class Admin_Page():
    def __init__(self):
        super().__init__()
        self.books = []
        #self.user_db = UserDatabase()
        self.run_display()
        
#création fenêtre "Admin"
Admin_Window = Tk()
#affichage de la page
Admin_Window.title('bibliotheque des 4 rives - Admin Page')
Admin_Window.geometry("1500x800")
Admin_Window.minsize(480,360)
Admin_Window.config(background='#15c3f2')
label_title = Label(Admin_Window, text='Bienvenue sur la page Admin de la Bibliothèque', font=("Arial",24),bg='#15c3f2',fg='red')
label_title.pack()
#création bouton "Gestion DB livres"
Frame_Button_1 =  Frame(Admin_Window, bg='#15c3f2')
Frame_Button_1.pack(side=LEFT, )
DB_Book_Button = Button(Frame_Button_1, text='Gestion DB Livres', font=("Arial",10), command= gestion_db_livres)
DB_Book_Button.pack(expand=YES, padx=40,)
#création bouton "Gestion DB Users"
Frame_Button_2 =  Frame(Admin_Window, bg='#15c3f2')
Frame_Button_1.pack(side=LEFT, )
DB_Users_Button = Button(Frame_Button_1, text='Gestion DB Utilisateurs', font=("Arial",10), command= gestion_db_users)
DB_Users_Button.pack(expand=YES, padx=40,)
Admin_Window.mainloop()

#Fonction pêrmettant de modifier la book_db (a completer pour la modification)
def gestion_db_livres():
    # Charger la base de données des livres depuis le fichier JSON
    with open('book.json', 'r') as f:
        livres_data = json.load(f)

    # Faites quelque chose avec la base de données des livres, par exemple afficher les données
    for book in books_data:
        print(book)
        
# Fonction permettant de modifier la user_db ( a completer pour ajouter la modification)

def gestion_db_users():
    #charger la base de données des livres depuis le fichier JSON
    with open('user.json', 'r') as f:
        users_data = json.load(f)
        
    for users in users_data:
        print(users)
