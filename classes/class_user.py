class User:
    def __init__(self, id, nom, prenom, mdp, email, isAdmin=False):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.mdp = mdp
        self.email = email
        self.isAdmin = isAdmin

    def afficher_infos(self):
        return f"Utilisateur: {self.nom} {self.prenom}\nID: {self.id}\nEmail: {self.email}\n"