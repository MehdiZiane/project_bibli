## initialisation de la class Book
class book:
    #initialisation de la méthode "book" en fonction de la DataBase
    def __init__(self,id_book,title,author,release_date,edition,literary_genre,first_cover,fourth_cover,resume):
        self.id_book = id_book
        self.title = title
        self.author = author
        self.release_date = release_date
        self.edition = edition
        self.literary_genre = literary_genre
        self.firts_cover = first_cover
        self.fourth_cover = fourth_cover
        self.resume = resume
        
# Affichage des livres    
    def bookOnScreen (self):
        print ("livre:",self.title,self.author,self.release_date,self.firts_cover,self.fourth_cover,self.resume)

# Fonction permetant de récupérer les livres de la base de données. ( a corriger en fonction de la création des listes)      
    def findABoook(list):
        book = []
        for element in list:
            book.append(element)
        return book
        # appel de la fonction bookOnScreen
        bookOnScreen(element)
        

# Initialisation de la Fonction de réservation ( a venir)


        
#Fonction principale ( a completer)
def main():

    main()
