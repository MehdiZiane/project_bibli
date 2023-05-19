class User:
    def __init__(self, id, nom, prenom, email):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email

    def afficher_infos(self):
        print("Utilisateur:", self.nom, self.prenom)
        print("ID:", self.id)
        print("Email:", self.email)


class Admin(User):
    def __init__(self, id, nom, prenom, email, role):
        super().__init__(id, nom, prenom, email)
        self.role = role

    def afficher_infos(self):
        super().afficher_infos()
        print("Role:", self.role)

def main():
    user1 = User(1, "Doe", "John", "john.doe@example.com")
    admin1 = Admin(2, "Smith", "Jane", "jane.smith@example.com", "Administrateur")

    user1.afficher_infos()
    print("----------")
    admin1.afficher_infos() 
if __name__ == "__main__":
    main()